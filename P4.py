# Aaron Garry, Mikelle Burnett, Blane Santilli, Asher Swartzberg, Henry Tuttle
# P4 – Retail Sales Data Import and Analysis
# Imports retail sales data from an Excel file, cleans it and uploads it to a PostgreSQL database. 
# It also allows users to query and summarize stored data by product category, A visual bar chart of sales by product is displayed as well.

from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot
import psycopg2

# Get user input
iUserInput = int(input(f'If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: '))

# Set excel file to variable
file_path = 'Retail_Sales_Data.xlsx'

# Create engine outside of if statements
username = 'postgres'
# this password will change per whoever is running it
password = '12345'
host = 'localhost'
port = '5432'
database = 'is303'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# Logic for import data input (1)
if iUserInput == 1:

    # Read excel file
    dfImportedFile = pd.read_excel(file_path)

    # Split name column into first_name and last_name columns
    dfSplitNames = dfImportedFile['name'].str.split("_", expand= True)

    # Insert new colums into original DF
    dfImportedFile.insert(1, 'first_name', dfSplitNames[0])
    dfImportedFile.insert(2, 'last_name', dfSplitNames[1])

    # Remove original 'name' column
    dfImportedFile = dfImportedFile.drop(columns=['name'])

    # Make sure category column matches product sold
    dictProductCategories = {
        'Camera': 'Technology',
        'Laptop': 'Technology',
        'Gloves': 'Apparel',
        'Smartphone': 'Technology',
        'Watch': 'Accessories',
        'Backpack': 'Accessories',
        'Water Bottle': 'Household Items',
        'T-shirt': 'Apparel',
        'Notebook': 'Stationery',
        'Sneakers': 'Apparel',
        'Dress': 'Apparel',
        'Scarf': 'Apparel',
        'Pen': 'Stationery',
        'Jeans': 'Apparel',
        'Desk Lamp': 'Houshold Items',
        'Umbrella': 'Accessories',
        'Sunglasses': 'Accessories',
        'Hat': 'Apparel',
        'Headphones': 'Technology',
        'Charger': 'Technology'}
    # .map function and above dictionary to fix categories
    dfImportedFile['category'] = dfImportedFile['product'].map(dictProductCategories)

    # Save results to table called 'sale' in is303 postgres database
    dfImportedFile.to_sql('sale', engine, if_exists='replace', index=False)

    # Print message upon completion
    print(f"You've imported the excel file into your postgres database.")

# Logic for data summary input (2)
elif iUserInput == 2:
    print(f"The following are all the categories that have been sold: ")

    # Read dataframe to do SQL
    dfImported = pd.read_sql_query("SELECT * FROM sale", con=engine)

    # Create list of all categories then print them all
    lstCategories = dfImported['category'].unique()

    index = 1 # initalize a counter for index in print statement 
    for category in lstCategories:
        print(f"{index}. {category}")
        index += 1

    # Get categories that user wants summarized and run calcuations for each one
    SelectedCategory = int(input(f"\nPlease enter the number of the category you want to see summarized: "))
    
    # Make it the variable in the list 
    SelectedCategory = lstCategories[SelectedCategory-1]
    print(SelectedCategory) # test to see if it worked 

    # Filter data for the selected category
    dfCategory = dfImported[dfImported['category'] == SelectedCategory]

    # sum total calculation
    dfCategory['total_price'] = dfCategory['quantity_sold']*dfCategory['unit_price']
    total_sales = dfCategory['total_price'].sum()
    
    # avg sale price
    average_price = dfCategory['unit_price'].mean()

    # total units sold
    total_units = dfCategory['quantity_sold'].sum()

    # print the calculations
    print(f"\nSummary for category: {SelectedCategory}")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Price: ${average_price:,.2f}")
    print(f"Total Units Sold: {total_units}")

    # display bar chart
    # use group by to get one row for each product then calc the sum of the total prices for each product 
    dfSales = dfCategory.groupby('product')['total_price'].sum()

    # create the actual bar chart 
    dfSales.plot(kind= 'bar') 

    # title
    plot.title(f"Total Sales in {SelectedCategory}")
# label for the x axis
    plot.xlabel("Product")
# label for the y axis
    plot.ylabel("Total Sales")
    # makes the chart appear on the screen
    plot.show()


    """
    # now start making the barchart and table
    # this was the start of the alternate way of doing things but I ended up going with Greg's method as it was easier
    # gives the table if it exists already 
    sqlDropTableIfExists = "DROP TABLE IF EXISTS sale";
    # now store the variable that holds the cursor
    cursor = conn.cursor()
    # run the tables commands if they exists/create one if it doesn't exist
    cursor.execute(sqlDropTableIfExists)
    # commit the changes from the buffer to the database
    conn.commit()
    """



#don't edit DEFAULT becasue that will be the primary key/id number  but this command will insert the records into the table 
# %s is simply a placeholder in a sql statement to pass in values into the statement
    sqlInsert = "INSERT INTO sales VALUES (DEFAULT, %s, %s)"





# Exit program
else:
    print(f"Closing the program.")
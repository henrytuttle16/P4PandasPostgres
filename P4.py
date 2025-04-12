from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot
import psycopg2

# Get user input
iUserInput = int(input(f'If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: '))

# Set excel file to variable
file_path = 'Retail_Sales_Data.xlsx'

<<<<<<< Updated upstream
=======
# Create engine outside of if statements
username = 'postgres'
# this password will change per whoever is running it
password = '12345'
host = 'localhost'
port = '5432'
database = 'is303'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

>>>>>>> Stashed changes
# Logic for import data input (1)
if iUserInput == 1:

    # Read excel file
    dfImportedFile = pd.read_excel(file_path)

    # Split name column into first_name and last_name columns
    dfSplitNames = dfImportedFile[file_path].str.split("_", expand= True)
    pass #need to insert new columns using .insert() and .drop to remove original column

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
    pass #need .map function and above dictionary to fix categories

    # Save results to table called 'sale' in is303 postgres database
    username = 'postgres'
    password = 'admin'
    host = 'localhost'
    port = '5432'
    database = 'is303'

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

    dfSplitNames.to_sql('sale', con=engine, if_exists='replace', index=True)

    # Print message upon completion
    print(f"You've imported the excel file into your postgres database.")

# Logic for data summary input (2)
elif iUserInput == 2:
    print(f"The following are all the categories that have been sold: ")

    # Print each category stored in database from 'sale' table
    pass

    # Get categories that user wants summarized and run calcuations for each one
    print(f"Please enter the number of the category you want to see summarized: ")
    pass
    # sum total calculation
    # avg calculation
    # total units calculation
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

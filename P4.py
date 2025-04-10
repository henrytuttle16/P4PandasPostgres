from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot
import psycopg2

# Get user input
iUserInput = int(input(f'If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: '))

# Set excel file to variable
file_path = 'Retail_Sales_Data.xlsx'

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

# Exit program
else:
    print(f"Closing the program.")

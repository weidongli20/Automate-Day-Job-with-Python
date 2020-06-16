# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('.')/'Resources'/'menu_data.csv'
sales_filepath = Path('.')/'Resources'/'sales_data.csv'

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, mode='r') as infile_menu:
    reader_menu = csv.reader(infile_menu)
    menu_header = next(reader_menu)
    menu=list(reader_menu)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, mode='r') as infile_sales:
    reader_sales = csv.reader(infile_sales)
    sales_header = next(reader_sales)
    sales=list(reader_sales)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sales_row in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    line_item_ID = sales_row[0]
    date = sales_row[1]
    credit_card_Number = sales_row[2]
    quantity= sales_row[3]
    item = sales_row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if item not in report:
        sales_metrics = {
            "01-count":0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }       
        report[item] = sales_metrics


    # @TODO: For every row in our sales data, loop over the menu records to determine a match
     for menu_row in menu:
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = menu_row[0]
        category = menu_row[1]
        description = menu_row[2]
        price = menu_row[3]
        cost = menu_row[4]

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if item == menu_item:
            # @TODO: Print out matching menu data
            print(f"{item} equals {menu_item}.")

            # @TODO: Cumulatively add up the metrics for each item key
            report[item]["01-count"] += quantity
            report[item]["02-revenue"] += price * quantity
            report[item]["03-cogs"] += cost * quantity
            report[item]["04-profit"] += profit * quantity


        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{item} does not equal {menu_item}! NO MATCH!")

    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"Total number of records in sales data:{row_count}")

# @TODO: Write out report to a text file (won't appear on the command line output)
output_path = Path('output.csv')
header = ["01-count", "02-revenue", "03-cogs", "04-profit"]

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    for row in report:
        metrics = [row["01-count"], row["02-revenue"], row["03-cogs"], row["04-profit"]]
        writer.writerow(metrics)

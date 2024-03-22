
SuperPy is a Supermarket Inventory Management Tool designed to handle buying and selling products, tracking inventory, and generating reports.

SuperPy Report

Technical Elements

1. Use of Rich Library for Improved UI
One notable technical element of this implementation is the integration of the Rich library to enhance the command-line interface (CLI) user experience. By utilizing Rich, the tool can display colored and formatted output, making it more visually appealing and user-friendly.

2. Visualization of Statistics Using Matplotlib

Another notable feature is the integration of Matplotlib for visualizing statistics. While the visualize_statistics function is a placeholder, integrating Matplotlib allows for the creation of various charts and graphs to represent inventory trends, revenue, and other relevant data.

3. Clear and Structured CLI Interface

The overall structure of the command-line interface adheres to the principles of clarity and user-friendliness. The use of argparse ensures a well-structured and organized CLI, with subcommands for different functionalities and clear descriptions in the --help section.

Key Components

-Global Variables:

today: Current date.
csv_folder: Folder containing CSV files.
bought_file: Path to the "bought.csv" file.
sold_file: Path to the "sold.csv" file.

-Rich Console:
Utilizes the rich library for an improved UI.

-Data Loading and Saving:

load_data(file_path, fieldnames=None): Loads data from a CSV file.
save_data(file_path, data, fieldnames): Saves data to a CSV file.

-Buying a Product:

buy_product(args): Adds a new entry for a bought product.

-Selling a Product:

sell_product(args): Adds a new entry for a sold product. Requires proper logic to find the correct product.

-Reporting Inventory:

report_inventory(now): Displays current or previous day's inventory.

-Advancing Time:

advance_time(days): Advances the current date by a specified number of days.

-Visualizing Statistics:

visualize_statistics(): Placeholder for implementing statistics visualization using Matplotlib.

-Creating Data File:

create_data_file(file_path): Creates an empty CSV file if it doesn't exist.

-Reporting Revenue:

report_revenue(args): Calculates and displays the total revenue.


Usage
Buying a Product


python superpy.py buy --product-name Orange --price 0.8 --expiration-date 2023-01-05

Selling a Product

python superpy.py sell --product-name Banana --price 1.5

Reporting Inventory

python superpy.py report inventory --now

python superpy.py report inventory --yesterday

Advancing Time

python superpy.py advance-time 5

Visualizing Statistics

python superpy.py visualize

Reporting Revenue

python superpy.py report revenue
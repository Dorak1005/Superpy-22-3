import csv
import argparse
from datetime import datetime, timedelta
from dateutil.parser import parse as parse_date
from rich.console import Console
import os

import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' or 'Agg'
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.ion()  # Enable interactive mode

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

#import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.savefig('plot.png')

# Global variables
TODAY = datetime.today().strftime('%Y-%m-%d')
CSV_FOLDER = "data/"
BOUGHT_FILE = os.path.join(CSV_FOLDER, "bought.csv")
SOLD_FILE = os.path.join(CSV_FOLDER, "sold.csv")

#Create a Rich Console for improved UI
console = Console()

def load_data(file_path, fieldnames=None, skip_header=True):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            if skip_header:
                next(reader)  # Skip the header row
            data = list(reader)
    except FileNotFoundError:
        pass

    return data

def save_data(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def buy_product(args):
    data = load_data(bought_file)
    new_entry = {
        'id': len(data) + 1,
        'product_name': args.product_name,
        'buy_date': today,
        'buy_price': args.price,
        'expiration_date': args.expiration_date
    }
    data.append(new_entry)
    save_data(bought_file, data)
    console.print(f"[green]Bought {args.product_name} for {args.price} on {today}[/green]")

def sell_product(args):
    data = load_data(sold_file)
    product_name = args.product_name
    sold_entry = {
        'id': len(data) + 1,
        'product_name': product_name,
        'sell_date': today,
        'sell_price': args.price
    }
    data.append(sold_entry)
    save_data(sold_file, data)
    console.print(f"[red]Sold {product_name} for {args.price} on {today}[/red]")

def report_inventory(args, console):
    if args.now:
        console.print("[cyan]Current Inventory:[/cyan]")
    else:
        console.print("[cyan]Inventory as of yesterday:[/cyan]")
    # Implement the logic to display inventory

#def report_inventory(now):
#    if now:
#        console.print("[cyan]Current Inventory:[/cyan]")
#    else:
#        console.print("[cyan]Inventory as of yesterday:[/cyan]")
#    # Implement the logic to display inventory

def display_inventory(date):
    bought_data = load_data(bought_file)
    filtered_data = [item for item in bought_data if parse_date(item['buy_date']).date() <= date]
    if filtered_data:
        console.print("[cyan]ID | Product Name | Buy Date | Buy Price | Expiration Date[/cyan]")
        for item in filtered_data:
            console.print(
                f"{item['id']} | {item['product_name']} | {item['buy_date']} | {item['buy_price']} | {item['expiration_date']}"
            )
    else:
        console.print("[red]No inventory data found[/red]")

def report_revenue(args, console):
    if args.today:
        console.print("Displaying revenue for today")
    elif args.yesterday:
        console.print("Displaying revenue for yesterday")
    else:
        console.print("Please specify either --today or --yesterday")

def report_profit(args, console):
    # Implement the logic to calculate and display profit
    console.print("[cyan]Profit Report:[/cyan]")
    
    # Load sold data with specific fieldnames and skip header
    sold_data = load_data(SOLD_FILE, fieldnames=['id', 'product_name', 'sell_date', 'sell_price'], skip_header=True)

    # Calculate total revenue
    total_revenue = sum(float(entry.get('sell_price', 0)) for entry in sold_data)

    console.print(f"Total Revenue: [green]${total_revenue:.2f}[/green]")

def advance_time(args, console):
    global TODAY
    today = datetime.strptime(TODAY, '%Y-%m-%d')
    today += timedelta(days=args.days)
    TODAY = today.strftime('%Y-%m-%d')
    console.print(f"[blue]Advanced time by {args.days} days. Today is now {TODAY}[/blue]")

def visualize_statistics():
    # Implement the logic to visualize statistics using Matplotlib
    pass

def visualize_data(args):
    print("Visualizing data")

    # Example data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Create a new figure
    plt.figure()

    # Plot the data
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Simple Line Graph')

    # Save the plot to a file
    plt.savefig('plot.png')

    # Show the plot
    plt.show()

def main():
    # Create the main parser
    parser = argparse.ArgumentParser(description='Superpy command line tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create a subparser for the "report" command
    report_parser = subparsers.add_parser('report', help='Report options')
    report_subparsers = report_parser.add_subparsers(dest='report_command', help='Report subcommands')

    # Create a subparser for the "inventory" subcommand
    inventory_parser = report_subparsers.add_parser('inventory', help='Inventory options')
    inventory_parser.add_argument('--now', action='store_true', help='Show current inventory')
    inventory_parser.set_defaults(func=report_inventory)

    # Create a subparser for the "revenue" subcommand
    revenue_parser = report_subparsers.add_parser('revenue', help='Revenue options')
    revenue_parser.add_argument('--today', action='store_true', help='Show revenue for today')
    revenue_parser.add_argument('--yesterday', action='store_true', help='Show revenue for yesterday')
    revenue_parser.set_defaults(func=report_revenue)

    # Create a subparser for the "profit" subcommand
    profit_parser = report_subparsers.add_parser('profit', help='Profit options')
    profit_parser.add_argument('--today', action='store_true', help='Show profit for today')
    profit_parser.set_defaults(func=report_profit)

    # Add subparser for 'advance-time'
    advance_time_parser = subparsers.add_parser('advance-time', help='Advance time')
    advance_time_parser.add_argument('days', type=int, help='Number of days to advance time')
    advance_time_parser.set_defaults(func=advance_time)

    # Create a subparser for the "visualize" subcommand
    visualize_parser = subparsers.add_parser('visualize', help='Visualize data')
    visualize_parser.set_defaults(func=visualize_data)

    # Create a subparser for the "buy" command
    buy_parser = subparsers.add_parser('buy', help='Buy a product')
    buy_parser.add_argument('--product-name', required=True, help='Name of the product')
    buy_parser.add_argument('--price', type=float, required=True, help='Price of the product')
    buy_parser.add_argument('--expiration-date', required=True, help='Expiration date of the product')
    buy_parser.set_defaults(func=buy_product)

    # Create a subparser for the "sell" command
    sell_parser = subparsers.add_parser('sell', help='Sell a product')
    sell_parser.add_argument('--product-name', required=True, help='Name of the product')
    sell_parser.add_argument('--price', type=float, required=True, help='Selling price of the product')
    sell_parser.set_defaults(func=sell_product)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        console = Console()  # Define the console object
        args.func(args, console)  # Pass console as an argument
    elif args.command == 'report':
        if args.subcommand == 'revenue':
            console = Console()  # Define the console object
            report_revenue(args, console)  # Pass console as an argument
        elif args.subcommand == 'profit':
            console = Console()  # Define the console object
            report_profit(args, console)  # Pass console as an argument
    elif args.command == 'advance-time':  # Handle advance-time command
        console = Console()  # Define the console object
        advance_time(args, console)  # Pass console as an argument
    elif args.command == 'visualize': # Handle visualize command
            console = Console() # Define the console object
            visualize_data(args, console) # Pass console as an argument
    else:
        print(f"Invalid command: {args.command}")

if __name__ == "__main__":
    main()

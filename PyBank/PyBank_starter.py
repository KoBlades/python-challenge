import csv
import os

# Ensure the "Resources" and "analysis" folders exist
os.makedirs("Resources", exist_ok=True)
os.makedirs("analysis", exist_ok=True)

# File paths
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_changes = []
previous_month_value = None
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Open and read the csv
try:
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)

        # Skip the header row
        header = next(reader)

        # Process each row of data
        for row in reader:
            # Track the total months and total net amount
            total_months += 1
            total_net += int(row[1])

            # Track the net change (difference between current and previous month)
            if previous_month_value is not None:
                net_change = int(row[1]) - previous_month_value
                net_changes.append(net_change)

                # Calculate the greatest increase in profits
                if net_change > greatest_increase[1]:
                    greatest_increase = (row[0], net_change)

                # Calculate the greatest decrease in losses
                if net_change < greatest_decrease[1]:
                    greatest_decrease = (row[0], net_change)

            # Set current month value as previous month value for the next iteration
            previous_month_value = int(row[1])

    # Calculate the average net change across the months
    average_net_change = sum(net_changes) / len(net_changes) if net_changes else 0

    # Generate the output summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_net_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    # Print the output to the terminal for debugging
    print(output)

    # Write the results to a text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

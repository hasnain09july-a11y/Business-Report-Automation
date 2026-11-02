import csv
from collections import defaultdict
from datetime import datetime

# 1. Store the input and output file names
INPUT_FILE = "sales_data.csv"
OUTPUT_FILE = "business_report.txt"

# 2. Read and analyze sales data
def analyze_sales():
    total_revenue = 0
    total_units = 0
    total_orders = 0

    product_revenue = defaultdict(float)

    with open(INPUT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = datetime.strptime(
                row["Date"], "%Y-%m-%d"
            ).date()

            product = row["Product"]
            quantity = int(row["Quantity"])
            price = float(row["Price"])

            revenue = quantity * price

            total_revenue += revenue
            total_units += quantity
            total_orders += 1

            product_revenue[product] += revenue

    if total_orders == 0:
        raise ValueError("No sales records found.")

    best_product = max(
        product_revenue,
        key=product_revenue.get
    )

    average_order_value = total_revenue / total_orders

    return {
        "revenue": total_revenue,
        "units": total_units,
        "orders": total_orders,
        "average": average_order_value,
        "best_product": best_product,
        "best_product_revenue": product_revenue[best_product]
    }

# 3. Generate a readable business report
def generate_report(data):
    report = f"""
================================
       BUSINESS SALES REPORT
================================

Total Revenue: ${data['revenue']:,.2f}
Total Units Sold: {data['units']}
Total Orders: {data['orders']}
Average Order Value: ${data['average']:,.2f}

Best-Selling Product by Revenue:
{data['best_product']}

Revenue from Best Product:
${data['best_product_revenue']:,.2f}

================================
       END OF REPORT
================================
"""
   
    return report

# 4. Save the report into a text file
def save_report(report):
    with open(OUTPUT_FILE, "w") as file:
        file.write(report)

# 5. Run the complete program
try:
    sales_data = analyze_sales()
    report = generate_report(sales_data)
    save_report(report)

    print("Business report generated successfully!")
    print(report)
    print(f"Report saved in {OUTPUT_FILE}")

except FileNotFoundError:
    print(f"Error: {INPUT_FILE} was not found.")

except (ValueError, KeyError) as error:
    print("Could not process the sales data:", error)

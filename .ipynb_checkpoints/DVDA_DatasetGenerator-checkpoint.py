# Dataset generator produced by Dr Kayode Owa for the ISYS40251 (Deriving Business Value from Data Analytics) module at Nottingham Trent University.
# Developed by Dr Kayode Owa for teaching and assessment activities in the ISYS40251 (Deriving Business Value from Data Analytics) module, School of Science & Technology, Nottingham Trent University.

import random
import pandas as pd
from datetime import datetime, timedelta

# --------------------------------------------------
# STATIC CHOCOLATE PRODUCT LIST (exactly 5 options)
# --------------------------------------------------
CHOCOLATE_PRODUCTS = [
    "Mint Chip Choco",
    "85% Dark Bars",
    "Peanut Butter Cubes",
    "Smooth Silky Salty",
    "99% Dark & Pure"
]

# --------------------------------------------------
# STATIC SALES PERSON LIST
# --------------------------------------------------
SALES_PERSONS = [
    "Jehu Rudeforth", "Van Tuxwell", "Gigi Bohling", "Jan Morforth",
    "Oby Sorrel", "Gunar Cockshoot", "Brien Boise", "Rafaela Blaksland",
    "Barr Faughny", "Mallorie Waber", "Karlen McCaffrey", "Marney O'Breem",
    "Beverie Moffet", "Curtice Advani", "Roddy Speechley"
]

# --------------------------------------------------
# STATIC COUNTRIES
# --------------------------------------------------
COUNTRIES = ["UK", "India", "Australia", "New Zealand", "USA", "Canada"]


# --------------------------------------------------
# RANDOM DATE GENERATOR WITHIN A YEAR
# --------------------------------------------------
def random_date():
    start_date = datetime(2022, 1, 1)
    random_days = random.randint(0, 365)
    d = start_date + timedelta(days=random_days)
    return d.strftime("%d-%b-%y")  # e.g., 07-Jul-22


# --------------------------------------------------
# DATA GENERATOR FUNCTION
# --------------------------------------------------
def generate_sales_data(n_rows):
    data = {
        "Sales Person": [],
        "Country": [],
        "Product": [],
        "Date": [],
        "Amount": [],
        "Boxes Shipped": []
    }

    for _ in range(n_rows):
        sp = random.choice(SALES_PERSONS)
        ct = random.choice(COUNTRIES)
        pr = random.choice(CHOCOLATE_PRODUCTS)
        dt = random_date()

        # amount e.g., $3,430
        amount = f"${random.randint(1000, 14000):,}"

        boxes = random.randint(10, 400)

        data["Sales Person"].append(sp)
        data["Country"].append(ct)
        data["Product"].append(pr)
        data["Date"].append(dt)
        data["Amount"].append(amount)
        data["Boxes Shipped"].append(boxes)

    return pd.DataFrame(data)


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------
if __name__ == "__main__":
    df = generate_sales_data(50)  # <-- change number of rows here
    print(df.head())

    df.to_excel("Chocolate_Sales_Data.xlsx", index=False)
    print("\nData saved to Chocolate_Sales_Data.xlsx")

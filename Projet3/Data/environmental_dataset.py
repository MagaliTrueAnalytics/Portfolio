import csv
import random
import uuid
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Lists for realistic test names
chemistry_tests = ["pH", "Turbidity", "Nitrate", "Phosphate", "Heavy Metals", "Chloride", "Sulfate", "Alkalinity", "Hardness", "TOC"]
microbiology_tests = ["Total Coliforms", "E. coli", "Fecal Streptococci", "Enterococci", "Pseudomonas aeruginosa", 
                     "Clostridium perfringens", "Legionella", "Heterotrophic Plate Count", "Cryptosporidium", "Giardia"]

# Function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to generate inconsistent date formats
def format_date(date, inconsistent=False):
    if inconsistent and random.random() < 0.03:  # 3% chance of wrong format
        formats = ["%d-%m-%Y", "%Y/%m/%d", "%m.%d.%Y"]
        return date.strftime(random.choice(formats))
    return date.strftime("%m/%d/%Y")

# Generate dataset
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 4, 19)
rows = []
num_rows = 1000

for _ in range(num_rows):
    request_id = str(uuid.uuid4())
    sample_date = random_date(start_date, end_date)
    num_tests = random.randint(1, 10)
    test_type = random.choice(["Chemistry", "Microbiology"])
    
    # Introduce typographical errors in Test_Type (1% chance)
    if random.random() < 0.01:
        test_type = random.choice(["Chemisty", "Microbio", "chemistry", "MICROBIOLOGY"])
    
    # Select test names based on test type
    test_list = chemistry_tests if test_type in ["Chemistry", "Chemisty", "chemistry"] else microbiology_tests
    sample_size = min(num_tests, len(test_list))  # Ensure sample size does not exceed list length
    test_names = random.sample(test_list, sample_size)
    test_names_str = ", ".join(test_names)
    
    # Calculate Final_CofA_Date (3–30 days after sample date)
    final_date = sample_date + timedelta(days=random.randint(3, 30))
    
    # Calculate revenue
    test_price = random.uniform(80, 300)
    revenue = round(num_tests * test_price, 2)
    
    # Introduce outliers in Revenue (2% chance)
    if random.random() < 0.02:
        revenue = random.choice([10, 5000, 10000])
    
    # Format dates with possible inconsistencies
    sample_date_str = format_date(sample_date, inconsistent=True)
    final_date_str = format_date(final_date, inconsistent=True)
    
    rows.append([request_id, sample_date_str, num_tests, test_type, test_names_str, final_date_str, revenue])

# Introduce missing values (5% chance per cell for specific columns)
for row in rows:
    if random.random() < 0.05:
        row[5] = "NaN"  # Final_CofA_Date
    if random.random() < 0.05:
        row[6] = "NaN"  # Revenue
    if random.random() < 0.05:
        row[4] = "NaN"  # Test_Names

# Introduce duplicates (2% of rows)
num_duplicates = int(num_rows * 0.02)
for _ in range(num_duplicates):
    rows.append(random.choice(rows))

# Write to CSV
with open("environmental_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Request_ID", "Sample_Received_Date", "Number_of_Tests", "Test_Type", "Test_Names", "Final_CofA_Date", "Revenue"])
    writer.writerows(rows)

print("Dataset generated successfully: environmental_dataset.csv")
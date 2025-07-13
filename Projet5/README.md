# 📊 Power BI Capstone Project – Tailwind Traders

This project is part of the [**Microsoft Power BI Data Analyst Professional Certificate**](https://www.coursera.org/professional-certificates/microsoft-power-bi-data-analyst) and showcases the full lifecycle of a Power BI solution developed for Tailwind Traders. It combines financial modeling, interactive reporting, cloud deployment, and time intelligence to simulate a real-world analytics environment.

## 📁 Project Overview

**Objective**: Analyze Tailwind Traders' sales and profitability data, design interactive Power BI reports, and simulate enterprise deployment using Power BI Service.

**Key Outputs**:
- Financial report in PDF
- Power BI Desktop file (.pbix)
- Cloud-deployed dashboard with mobile layout, alert, and subscription features

## 🔍 Dataset Sources

1. `Sales.xlsx` – Product-level transaction data (Quantity, Tax, Category, etc.)
2. `Purchases.xlsx` – Procurement and return records (Supplier, Dates, Return Policy)
3. `Countries.xlsx` – Country metadata with exchange IDs
4. `Exchange Data.csv` – Generated via Python in VS Code Cloud to overcome Power BI Desktop constraints

➡️ *Manual addition of calculated columns (`Gross Revenue`, `Net Revenue`) prior to data import.*

## 🛠️ Data Modeling

- **Snowflake schema** built in Power BI
- DAX-generated **Calendar table** for Time Intelligence
- `Sales USD` table created via DAX for currency normalization
- Key measures: YTD Profit Margin, Quarterly Margin, Median Gross Revenue

## 🎨 Report Design

### Page 1 – *Sales Overview*
- KPIs: Quantity Purchased, Median Sales, Stock
- Charts: Loyalty Points by Country, Product Sales, Sales Trends
- Country slicer for dynamic filtering

### Page 2 – *Profit Overview*
- KPIs: YTD Profit Margin, Net & Gross Revenue
- Charts: Profit by Product, Margin by Country, Time-Based Margin Trends

## ☁️ Deployment in Power BI Service

- 📌 Dashboard created via pinning key visuals
- 📱 Mobile layout optimized using Mobile View editor
- 🔔 Alert set for `Gross Revenue < $400`
- 📬 Subscriptions configured:
  - **Sales Weekly** – Sundays 5:00 AM
  - **Sales Monthly** – First day of month 5:00 AM
  - **Profit Weekly** – Mon/Wed/Fri 6:00 AM

## 📦 Deliverables

- `Tailwind_Traders_Report.pdf` – Exported static report
- `Tailwind_Traders_Analytics.pbix` – Interactive Power BI file
- 📸 Screenshots: Dashboard view, Mobile layout, Alert & subscription settings

## 🗂️ Project Hierarchy & Folder Description

This project is organized into three main folders, each playing a distinct role in the analytics workflow:

### 📁 Data/
Contains all raw and transformed datasets used in Power BI
These files serve as the foundation of the data model and were imported into Power BI Desktop using the *Get Data* feature.

---

### 📁 Notebook/
Includes one Jupyter Notebook acting as a step-by-step **SOP (Standard Operating Procedure)** for the entire project:
- `PowerBI_Capstone_Project.ipynb`

The notebook documents key stages from data preparation to DAX modeling, visual design, and deployment, making it an ideal guide for learners, collaborators, or recruiters.

---

### 📁 Report/
Houses final deliverables and result documentation:
- `Tailwind_Traders_Report.pdf` – Exported static version of the report  
- `Tailwind_Traders_Analytics.pbix` – Power BI Desktop file  
- `Dashboard_Screenshot.png` – Cloud dashboard pinned from report  
- `Mobile_Layout_Screenshot.png` – Mobile view version  
- `Subscriptions_Screenshot.png` – Email subscription setup
- `Alert_Screenshot.png` – Alert setup
  
These assets demonstrate the completeness of the analytics solution, from insight generation to stakeholder delivery and cloud publishing.

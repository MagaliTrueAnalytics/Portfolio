# Shapefile Dataset for Choropleth Maps

## 📌 Overview
This directory contains a **Shapefile dataset** that provides geographical boundaries for countries.  
It is essential for visualizing data geographically, particularly for **choropleth maps** in Python using **Geopandas**.

## 🌍 Purpose
The files in this folder enable the creation of **choropleth maps**, which represent variations in data across different geographical locations.  
For example, you can use this dataset to **display sales distribution by country** or **analyze regional trends** in a dataset.

## 📂 Files Included
A Shapefile dataset consists of multiple files that must be **stored together** to function properly:
- **`.shp`** → Stores the geometric shapes (country boundaries).
- **`.dbf`** → Contains attribute data (country names, population, etc.).
- **`.shx`** → Indexes geometric data for faster access.
- **`.prj`** → Defines the coordinate reference system (CRS) for spatial alignment.

## 🛠️ How to Use in Geopandas
To read the shapefile in **Geopandas**, ensure all necessary files are present and use the following Python code:

```python
import geopandas as gpd

# Load the shapefile
shapefile_url = "https://raw.githubusercontent.com/MagaliTrueAnalytics/Portfolio/main/Shapefile/ne_110m_admin_0_countries.shp"
world = gpd.read_file(shapefile_url)

# Display the first rows to check data structure
print(world.head())


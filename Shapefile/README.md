<h2>Shapefile & GeoJSON Dataset for Choropleth Maps</h2>

📌 **Overview**

This directory contains **geographical boundary datasets** that can be used for **choropleth maps** in Python with **Geopandas**. The dataset is available in Shapefile format, but an **easier-to-use GeoJSON** version is also provided.

🌍 **Purpose**

These files enable the visualization of data distribution across countries, such as sales by region or geographical trends. For many applications, the **GeoJSON format** is preferred because it simplifies **loading, filtering, and integration with web-based visualizations**.

📂 **Files Included**

- **Shapefile (requires all components together)**
.shp → Geometric shapes (country boundaries).

.dbf → Attribute data (population, names, etc.).

.shx → Indexes for geometric data.

.prj → Defines the coordinate reference system (CRS).

- **GeoJSON (simplified alternative)**
.geojson → A single file containing both geometry and attributes. 💡 Advantage: Easier to handle in Python and JavaScript, with direct JSON parsing.

## 🛠️ How to Use in Geopandas
📍**Option 1: Using the Shapefile**

import geopandas as gpd

- **Load the Shapefile (requires all files in the same folder)**

shapefile_url = "https://raw.githubusercontent.com/MagaliTrueAnalytics/Portfolio/main/Shapefile/ne_110m_admin_0_countries.shp"

world = gpd.read_file(shapefile_url)

- **Display data structure**

print(world.head())

📍**Option 2: Using the GeoJSON (Recommended)**

import geopandas as gpd

- **Load the GeoJSON version**

geojson_url = "https://raw.githubusercontent.com/MagaliTrueAnalytics/Portfolio/main/Shapefile/ne_110m_admin_0_countries.geojson"
world_geojson = gpd.read_file(geojson_url)

- **Display data structure**

print(world_geojson.head())

💡 Why use GeoJSON? ✅ Requires only one file instead of multiple Shapefile components ✅ Easier integration with web-based visualizations (D3.js, Leaflet, etc.) ✅ Supports direct JSON operations for faster processing



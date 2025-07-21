##  🌿Cannabis Market Snapshot: Québec’s SQDC Landscape (July 2025)

This Power BI project explores the cannabis retail landscape in Québec as of **July 17, 2025**, with a focus on data available through the **Société Québécoise Du Cannabis (SQDC)**.

### 🔍 Scope of the Analysis
The project offers a sectoral snapshot, combining manually collected and webscraped data to highlight key trends and market dynamics:
- **Product categories** analyzed: *dried flower*, *milled*, *pre-rolls*, and *hashish* (representing >80% of SQDC's catalog)
- **Price structures** across categories, strains, dominance (THC/CBD/Balanced), and producers
- **Provincial breakdown of producers** from Québec vs other Canadian provinces
- **Retail footprint**: opening dates and expansion trend of SQDC stores
- **Brand and producer relationships**, captured through multi-source data modeling

### 📦 Data Sources
- **SQDC website** (manual collection): product catalog, pricing, dominance profiles, strains, categories, producers
- **Weedcrawler.ca** (authorized web scraping): detailed data on SQDC store network, product availability, brand distribution

### 📁 Project Structure

As with other portfolio projects, the repository includes three main folders:  
- `/Data` — contains the raw `.csv` and `.xlsx` datasets  
- `/Notebook` — includes a structured Jupyter Notebook documenting each step from data collection to analysis and report creation, written as a SOP-style workflow  
- `/Report` — hosts the Power BI `.pbix` file, a static `.pdf` version of the dashboard, and a Canva-formatted report for broader readability (french only)

🛈 Notes on Producer/Brand Labeling  
All names are anonymized in the PDF and Canva reports for public neutrality.  
Tooltips in Power BI reveal original names only for internal reference and personalized insight.

### 🖥️ Viewing the Power BI Report
The interactive report file (.pbix) can be opened and explored using the free version of Power BI Desktop, available for download here: [Download Power BI Desktop](https://www.microsoft.com/en-us/power-platform/products/power-bi/downloads)

This format offers full interactivity, including dynamic filters, tooltips, and rich analytics. It makes the dashboard fully accessible to all producers—including small-scale actors and those who haven't yet embraced a fully data-driven culture.

### 🛡️ Intellectual Property & Usage Disclaimer

This project, **Cannabis Market Snapshot: Québec’s SQDC Landscape (July 2025)**, was developed as part of an independent data analytics initiative. It includes original data processing scripts, Power BI semantic modeling, and interactive dashboards based on both publicly available data and authorized web scraping.

All analyses, visualizations, and code contained in this repository are the intellectual work of the project author and are shared for educational and exploratory use only.

Please note:

- The webscraped data from [Weedcrawler.ca](https://quebec.weedcrawler.ca/) was collected with permission from its creator, **Alexandre Voyer**. Commercial reuse of this data is strictly prohibited unless explicit consent is obtained.
- All manual data collections from the SQDC website comply with publicly visible content usage. No user-specific or private information was scraped.
- This repository does **not** endorse or promote any specific cannabis products or brands. It is intended solely for market analysis, benchmarking, and strategic exploration within a regulated and transparent framework.

If you wish to reference, reuse, or collaborate based on the contents of this project, please credit accordingly or reach out directly via GitHub. All contributions, discussions, and ethical usage are welcome and appreciated 🌿

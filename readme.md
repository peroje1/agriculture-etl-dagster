# Agricultural Yield Analytics Dashboard

This project is an end-to-end data analytics pipeline designed to extract insights from large-scale crop yield data. It combines Python-based data engineering with MySQL storage and interactive Power BI visualizations.

## Tech Stack

- **Python (pandas)** – Data cleaning and aggregation
- **MySQL** – Database for storing raw and aggregated data
- **Power BI** – Business intelligence dashboard for exploration and insights
- **SQLAlchemy / Power Query** – Data connectors between Python, SQL, and Power BI

## Workflow Overview

1. **Data Preparation**
   - Input: Raw CSV with 1M+ rows of crop yield and environmental features
   - Original CSV file is not present in git due to large size
   - Processing: Cleaned and transformed using pandas
     - Binning continuous variables (rainfall, temperature, etc.)
     - Creating efficiency metrics and categorical flags
     - Grouped aggregations by crop, region, and weather

2. **Database Integration**
   - Transformed data exported into MySQL using SQLAlchemy
   - Aggregated tables stored with consistent naming (`agri_*`)

3. **Power BI Reporting**
   - Data imported from MySQL and CSV
   - Additional cleaning done with transform data
   - Interactive dashboard built with:
     - KPI cards (average yield, top crop/region)
     - Bar and column charts (by crop, soil, weather)
     - Pie charts
     - Slicers for filtering (Weather)
     - Raw CSV used for trend lines and scatter plots

## Example Insights

- High rainfall and moderate temperatures are correlated with better yields
- Specific crops perform better in certain regions and soil types
- Effects of irrigation and fertilizer on crop yield

See attached PDF for dashboard visuals and explanation.


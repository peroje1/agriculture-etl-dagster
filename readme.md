# Agricultural Yield Analytics Dashboard

This project is an end-to-end data analytics pipeline designed to extract insights from large-scale crop yield data. It combines Python-based data engineering with MySQL storage and interactive Power BI visualizations.

## Tech Stack

- **Python (pandas)** 
- **MySQL** 
- **Power BI** 
- **SQLAlchemy / Power Query** 
- **Dagster

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
4. **Optional orchestration via Dagster** 
     -modular jobs (clean/load/transform/extract)
     -sensors (checks for new files)
     -schedules (runs weekly)

## Example Insights

- High rainfall and moderate temperatures are correlated with better yields
- Specific crops perform better in certain regions and soil types
- Effects of irrigation and fertilizer on crop yield

[Click here to view the dashboard (PDF)](dashboard.pdf)


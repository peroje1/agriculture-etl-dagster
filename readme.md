# Agricultural Etl Pipeline with Dagster

An end-to-end data analytics pipeline designed to extract insights from large-scale crop yield data. This project combines Python-based data engineering, MySQL storage, and interactive Power BI visualizations.

## Tech Stack

- Python (pandas)  
- MySQL  
- Power BI  
- SQLAlchemy / Power Query  
- Dagster (optional orchestration)

## Workflow Overview

1. **Data Preparation**  
   - Input: Raw CSV file with 1M+ rows of crop yield and environmental features (not included in the repo due to large size)  
   - Processing with pandas:  
     - Data cleaning and transformation  
     - Binning continuous variables (rainfall, temperature, etc.)  
     - Creating efficiency metrics and categorical flags  
     - Grouped aggregations by crop, region, and weather conditions  

2. **Database Integration**  
   - Export transformed and aggregated data into MySQL using SQLAlchemy  
   - Aggregated tables stored with consistent naming convention (`agri_*`)  

3. **Power BI Reporting**  
   - Import data from MySQL and CSV files  
   - Perform additional cleaning and transformations in Power Query  
   - Build interactive dashboard featuring:  
     - KPI cards (e.g., average yield, top crop, top region)  
     - Bar and column charts segmented by crop, soil type, and weather  
     - Pie charts for categorical distributions  
     - Slicers for dynamic filtering (e.g., by weather conditions)  
     - Trend lines and scatter plots using raw CSV data for detailed analysis  

4. **Optional Orchestration via Dagster**  
   - Modular jobs to handle cleaning, loading, transforming, and extraction steps  
   - Sensors to detect new input files  
   - Scheduled runs (e.g., weekly) for automated pipeline execution  

## Example Insights

- High rainfall combined with moderate temperatures correlates with higher crop yields  
- Certain crops perform better in specific regions and soil types  
- Positive impact of irrigation and fertilizer use on yield efficiency  

[View the dashboard (PDF)](dashboard.pdf)

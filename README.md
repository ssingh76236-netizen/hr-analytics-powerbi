# HR Analytics Dashboard — Workforce & Sales Analysis
Built this to understand what real HR reporting looks like inside a company. 
Modeled after the kind of dashboards HR and Sales teams actually use to track 
people, performance, and attrition.

 What This Does
Most HR teams are flying blind — they know someone quit, but not why, when, 
or which department is bleeding the most. This dashboard tries to answer that.

4 pages, each solving a different business question:
- Overview — How many people do we have? How many left?
- Attrition — Who's leaving, why, and how early?
- Sales Performance — Are we hitting targets? Which region is strongest?
- Productivity — Does training actually lead to more deals closed?

 [Tech Stack] Tool : What I used it for 
- Python (Pandas, Faker) : Generated 10,000+ rows of realistic HR data.
- MySQL : Stored and structured data across 5 tables.
- Power BI : Built all 4 dashboard pages.
- DAX : Wrote custom measures for KPIs.


 Features
- Row Level Security — HR Manager of Sales sees only Sales data
- Drill through reports
- Slicers for month, year, region
- Intentionally messy data cleaned in Power Query (realistic workflow)


## Dashboard Screenshots
### Overview
![Overview](screenshots/01_Overview.png)
### Attrition Deep Dive
![Attrition](screenshots/02_Attrition.png)
### Sales Performance
![Sales](screenshots/03_Sales_Performance.png)
### Productivity
![Productivity](screenshots/04_Productivity.png)

## Files
 `generate_data.py` : Generates employee table with realistic mess 
 `generate_tables.py` : Generates attrition, sales, productivity, headcount tables 
 `HR Dashboard.pbix` : Power BI file — open in Power BI Desktop 

## How to Run Locally
1. Install MySQL and create database `hr_analytics_db`
2. Run `generate_data.py` then `generate_tables.py`
3. Open `HR Dashboard.pbix` in Power BI Desktop
4. Update MySQL connection to your local credentials


*Data is fully synthetic — generated using Python Faker with intentional 
inconsistencies to simulate real export quality.*

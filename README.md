# End-to-End Retail Operations Analytics Pipeline

## Project Overview
This project demonstrates a complete, end-to-end enterprise data analytics workflow. It simulates a real-world retail environment where raw transactional data is extracted from a relational database, merged with offline HR mapping files, cleaned using Python, and visualized in an executive dashboard. 

## Technology Stack
* **Database Management:** MySQL (Data Modeling, Extraction)
* **Ad-Hoc Mapping:** Microsoft Excel (`XLOOKUP`)
* **Data Engineering:** Python (`pandas`, VS Code)
* **Business Intelligence:** Tableau Public

## Pipeline Architecture

### Phase 1: Database Extraction (SQL)
* Designed and populated a simulated local database with `Transactions` and `Store_Locations` tables.
* Wrote an extraction query utilizing `INNER JOIN` to merge fragmented sales and regional data.
* Engineered a new column using a `CASE` statement to dynamically categorize sales into transaction tiers (High Value, Standard, Review Required).

### Phase 2: Business Logic Integration (Excel)
* Simulated an offline HR environment by building a standalone `Manager_Directory`.
* Utilized `XLOOKUP` to seamlessly map regional managers to their respective Store IDs alongside the exported SQL database extract.

### Phase 3: Data Engineering & Cleaning (Python)
* Deployed a Python script using the `pandas` library to ingest the merged Excel workbook.
* Standardized formatting by converting string dates into proper `datetime` objects.
* Handled intentional data entry errors by locating and filling missing (`NULL`) financial values with standard integers.
* Exported a validated, production-ready `.csv` file.

### Phase 4: Executive Dashboarding (Tableau)
* Connected the cleaned dataset to Tableau Public.
* Developed a horizontal bar chart to rank regional manager performance based on total revenue generation.
* Applied the SQL-engineered `transaction_tier` logic to dynamically color-code the visualization.

## Files in this Repository
* `extraction_query.sql`: The database creation, insertion, and `JOIN` query script.
* `data_cleaner.py`: The Python pandas script used for data validation and cleaning.
* `Tableau_Ready_Data.csv`: The final processed dataset used for visualization.

## Final Visualization
[Click here to view the interactive Tableau Dashboard] https://public.tableau.com/authoring/Retail_Analytics_Dashboard_17920030753790/Sheet1#2


---

Weather Data Processing Pipeline

This project builds a simple Python pipeline to ingest, clean, transform, and analyze weather data from a CSV file.

Features:

* Load and clean data from "weather\_data.csv"
* Standardize date formats and handle missing values
* Add temperature in Fahrenheit
* Filter out invalid weather conditions
* Save cleaned data and generate summary reports
* (Bonus) Bar chart of average temperature per city

Quick Start:
Run these commands to set up and execute the project:

```
python -m venv venv
source venv/bin/activate   (On Windows: venv\Scripts\activate)
pip install -r requirements.txt
python app.py
# Or run the notebook:
jupyter notebook take_home.ipynb
```

Outputs:

* outputs/transformed\_weather\_data.csv — cleaned data
* outputs/top5\_temperatures.txt — top 5 highest temperatures
* outputs/average\_temperature\_per\_city.png — bar chart visualization

Dependencies:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn

Install with:

```
pip install -r requirements.txt
```

Notes:

* Dates converted to YYYY-MM-DD format
* Missing numeric values replaced with city averages
* Rows with “Unknown” weather conditions are excluded

---


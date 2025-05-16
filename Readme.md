````markdown
# Weather Data Processing Pipeline

This project is a simple data pipeline to ingest, clean, transform, and analyze weather data using Python.

## Features

- Load data from `weather_data.csv`
- Clean and format the data (handle missing values, standardize date format)
- Add a new column: temperature in Fahrenheit
- Filter out invalid entries
- Save cleaned data and generate a report
- (Bonus) Create a bar chart of average temperature per city

## How to Run

### 1. Set up environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2. Run the script

```bash
python app.py
```

Or use the Jupyter notebook:

```bash
jupyter notebook take_home.ipynb
```

## Output

* `outputs/transformed_weather_data.csv`: Cleaned data
* `outputs/top5_temperatures.txt`: Top 5 highest temperatures
* `outputs/average_temperature_per_city.png`: Bar chart of average temperature

## Dependencies

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn

Install with:

```bash
pip install -r requirements.txt
```

## Notes

* Dates are cleaned and unified to `YYYY-MM-DD` format
* Missing values are filled with the column mean
* “Unknown” weather conditions are filtered out

```

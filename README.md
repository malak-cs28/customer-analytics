# Uber NYC Trip Data Pipeline

## Team Members
- Name: Malak Mohamed AbdelMamid
- ID: 231000786

- Name: Haneen Abdelmeeged Mohamed
- ID:  231002231

- Name: Malak Wael Ahmed 
- ID: 231001842

- Name: Fady Ragaie Nahoum
- ID: 21100140
---

## Project Description
This project builds a complete Docker-based data pipeline using the Uber NYC trip dataset.

The pipeline performs:
- Data ingestion
- Data preprocessing
- Textual analytics
- Data visualization
- K-Means clustering

---

## Dataset
Dataset used:
- `uber-raw-data-jun14.csv`

Dataset columns:
- `Date/Time`
- `Lat`
- `Lon`
- `Base`

---

# Project Structure

- customer-analytics/
- ├── Dockerfile
- ├── ingest.py
- ├── preprocess.py
- ├── analytics.py
- ├── visualize.py
- ├── cluster.py
- ├── summary.sh
- ├── README.md
- ├── data/
- │   └── uber-raw-data-jun14.csv
- └── results/


---

## Preprocessing Steps

### Data Cleaning
- Removed missing values
- Removed duplicate rows
- Converted `Date/Time` to datetime format
- Removed invalid latitude/longitude values

### Feature Transformation
- Extracted `hour`, `day`, and `weekday`
- Encoded `Base` column
- Scaled numeric columns

### Discretization
- Converted `hour` into `time_period`:
  - Night
  - Morning
  - Afternoon
  - Evening

### Dimensionality Reduction
- Used feature selection to keep meaningful columns

---

## Analytics Insights
The following files are generated:
- `insight1.txt`: Most active time period
- `insight2.txt`: Most active Uber base
- `insight3.txt`: Most active weekday

---

## Visualization
Three plots are created and saved in:
- `summary_plot.png`

Plots:
- Trips by time period
- Trips by base
- Pickup locations scatter plot

---

## Clustering
K-Means clustering is applied using:
- Latitude
- Longitude
- Hour

Results are saved in:
- `clusters.txt`

---

## Docker Build and Run Commands

From the project root:

```bash
docker build -t customer-analytics .
docker run -it --name customer_analytics_container customer-analytics
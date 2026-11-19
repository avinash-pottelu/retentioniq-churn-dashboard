@'
# RetentionIQ

A customer churn analytics dashboard built with Python and Streamlit.

## Status
Day 1 complete: initial dashboard running locally.

## Current features
- Upload a Telco Customer Churn CSV file
- Display total customers
- Display churned customer count
- Calculate historical churn rate
- Preview the uploaded data

## Technologies
- Python
- pandas
- Streamlit

## Run locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the app:

```bash
python -m streamlit run app.py
```

Upload the Telco Customer Churn CSV through the dashboard.

## Dataset
Download the dataset from:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The dataset is not included in this repository.

## Planned improvements
- Data cleaning and validation
- Customer churn visualizations
- Churn prediction model
- Model evaluation and explanations

## Limitations
This version displays historical churn metrics.
It does not yet predict future churn.
'@ | Set-Content README.md
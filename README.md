# Supply Chain & Delivery Performance Analytics

## Project Overview

This project analyzes supply chain operations to understand delivery performance, sales, profitability, and order fulfillment. The objective is to identify delivery delays, evaluate shipping methods, and discover business insights that can help improve operational efficiency.

The project uses Python for data cleaning and exploratory data analysis (EDA), and Power BI to build an interactive business dashboard.

## Tools & Technologies

- **Python** — Data cleaning and exploratory data analysis
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **VS Code** — Python development environment
- **Power BI** — Interactive dashboard and visualization
- **Excel/CSV** — Data storage and inspection

## Dataset Overview

- **Dataset:** Supply Chain / DataCo Supply Chain Dataset
- **Records:** 180,519 rows
- **Time Period:** January 2015 – January 2018
- **Format:** CSV

The dataset contains order, shipping, product, sales, profit, customer, and delivery-related information.

## Project Objectives

- Analyze overall sales and profitability.
- Identify late deliveries and delivery delays.
- Compare scheduled shipping time with actual shipping time.
- Evaluate shipping methods and their delivery performance.
- Identify product categories and markets contributing to sales.
- Understand order distribution across customer segments and departments.
- Present findings through an interactive Power BI dashboard.

## Python Data Cleaning & Analysis

Python was used in VS Code to prepare and analyze the dataset.

### 1. Data Loading

Loaded the CSV dataset using Pandas with the appropriate encoding.

### 2. Data Preparation

- Standardized column names by replacing spaces with underscores.
- Removed unnecessary columns, including personal customer information and unused geographic fields.
- Checked data types and missing values.
- Checked duplicate records and duplicate order-item identifiers.
- Converted order and shipping date columns into datetime format.
- Checked whether shipping dates occurred before order dates.

### 3. Exploratory Data Analysis

Analyzed the dataset to understand:

- Sales and profit distribution.
- Product category performance.
- Sales by market and customer segment.
- Shipping method performance.
- Scheduled versus actual shipping days.
- Delivery delays and late-delivery risk.
- Negative-profit transactions.

### 4. Delivery Performance Calculation

Created a delivery delay calculation by comparing actual shipping days with scheduled shipping days.

**Formula:**

`Delivery Delay = Actual Shipping Days - Scheduled Shipping Days`

Interpretation:

- Positive value: Delivery took longer than scheduled.
- Zero: Delivery matched the scheduled duration.
- Negative value: Delivery was faster than scheduled.

## Key Findings

The following findings were identified during the analysis:

- The dataset contains **180,519 records**.
- Total sales were approximately **36.78 million**.
- Recorded profit was approximately **3.97 million**.
- Overall recorded profit margin was approximately **10.78%**.
- Negative-profit transactions were identified and analyzed.
- Shipping methods showed different average delivery-delay patterns.
- Central Asia and Central Africa had relatively high average delivery delays among the regions analyzed.
- Product categories, markets, and customer segments showed different sales contributions.

*Note: These figures reflect the project's recorded analysis and may depend on the cleaning steps and calculation definitions used.*

## Power BI Dashboard

The interactive dashboard contains three pages.

### Page 1 — Business Overview

Provides a high-level summary of supply chain performance.
<img width="933" height="548" alt="business_overview" src="https://github.com/user-attachments/assets/8bb79edf-51e4-4713-9379-a3ab363e7a66" />


Includes:
- Overall sales and profitability KPIs.
- Order and business performance summaries.
- Sales distribution across product categories, markets, and customer segments.

### Page 2 — Delivery Performance

Focuses on shipping efficiency and delivery delays.
<img width="937" height="549" alt="delivery_performance" src="https://github.com/user-attachments/assets/b578e736-e42d-49d3-859c-cdb837fe06c7" />

Includes:
- Actual versus scheduled shipping performance.
- Delivery-delay analysis.
- Shipping method comparisons.
- Late-delivery risk analysis.
- Regional delivery performance.

### Page 3 — Sales & Profitability

Examines financial performance across different business dimensions.
<img width="936" height="548" alt="sales and profitability" src="https://github.com/user-attachments/assets/648410e3-6bc9-4eb4-805f-cf36c0021a8c" />

Includes:
- Sales by product category.
- Profitability analysis.
- Sales by market and customer segment.
- Negative-profit transaction analysis.

The dashboard is designed to help users explore performance by using available filters and visual interactions.

## Business Value

This analysis can help supply chain and operations teams:

- Identify shipping methods associated with delivery delays.
- Monitor late-delivery risk.
- Understand sales and profit contribution across business segments.
- Investigate transactions with negative profit.
- Identify areas where delivery operations and profitability may need improvement.

## Project Structure

```text
Supply-Chain-Delivery-Performance-Analytics/
│
├── README.md
├── requirements.txt
├── supply_chain_analysis.py
|── data/supplychain-compressed.zip
├── powerbi/
│   └── supply_chain.pbix
│
└── screenshots/
    ├── business_overview.png
    ├── delivery_performance.png
    └── sales_profitability.png



## How to Run the Python Analysis

### Step 1 — Install Python Libraries

Open the VS Code terminal and run:

```bash
pip install pandas numpy openpyxl
```

### Step 2 — Keep the Dataset and Python File Together

Place `supplychain.csv` and your Python analysis script in the same project folder, or update the dataset path in your script.

### Step 3 — Run the Script

```bash
python supply_chain_analysis.py
```

The script performs the data preparation and analysis defined in the Python file.

### Step 4 — Open the Power BI Dashboard

Open the `.pbix` file in Power BI Desktop to explore the completed dashboard.

## Skills Demonstrated

- Python programming
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Pandas data manipulation
- Date and delivery-delay calculations
- Sales and profitability analysis
- Business problem-solving
- Power BI dashboard development
- Data visualization and insight communication

## Conclusion

The Supply Chain & Delivery Performance Analytics project demonstrates how Python and Power BI can be used together to analyze operational and financial data. It highlights delivery performance, shipping efficiency, sales contribution, and profitability to support data-driven business decisions.

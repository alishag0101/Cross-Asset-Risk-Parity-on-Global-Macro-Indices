# Cross-Asset Risk Parity on Global Macro Indices

This project implements a cross-asset risk parity strategy using:

- **Factor Synthesis**: Identifies key macroeconomic drivers (e.g. interest rates, inflation, GDP growth) for diversifying equity, bond, FX, and commodity exposures.
- **Adaptive Risk Budgeting**: Maintains a stable 10% volatility threshold across asset classes with dynamic volatility targeting.
- **Machine Learning Integration**: Deploys a random forest framework to forecast asset returns daily, realising a ~15% improvement in Sharpe ratio from 2022 to 2024 compared to standard risk parity approaches.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [License](#license)

## Features

- **Factor Synthesis**:  
  - Reads macroeconomic time-series data (e.g. interest rates, inflation, GDP)  
  - Normalises and transforms data for principal component or correlation-based factor identification

- **Adaptive Risk Budgeting**:  
  - Dynamically rebalances portfolio weights to maintain target volatility  
  - Supports multiple asset classes (equity, bonds, FX, commodities)

- **Machine Learning Forecast**:  
  - Random forest model for daily return prediction  
  - Uses macro factors and historical asset data as features

## Installation

1. **Clone the Repository**  
   First, clone the repository to your local machine:
   
   ```bash
   
   git clone https://github.com/alishag0101/Cross-Asset-Risk-Parity-on-Global-Macro-Indices.git
   cd Cross-Asset-Risk-Parity-on-Global-Macro-Indices
2. **Install Dependencies** 
  Install the required Python libraries using pip:

   ```bash
   
   pip install -r requirements.txt

3. **Prepare Real Data**
  Replace the mock data in data/sample_macro_data.csv with real macroeconomic data. Ensure the CSV file has the following columns:
  Date: Timestamps of data points.
  InterestRates, Inflation, GDPGrowth: Macro indicators.
  EquityReturns, BondReturns, FXReturns, CommodityReturns: Asset returns.
Ensure all columns have consistent formatting.

## Usage

1. **Run the Full Pipeline**
  To process the data, synthesize factors, apply adaptive risk budgeting, and integrate machine learning, run:
   ```bash
    python src/main.py
  This script will:
    1. *Perform factor synthesis using macroeconomic indicators.*
    2. *Generate dynamically adjusted portfolio weights with risk budgeting.*
    3. *Forecast future returns using machine learning.*
2. **Optionally, Explore the Data**
  Open the Jupyter notebook for factor analysis and visualization:
    ```bash
     jupyter notebook notebooks/factor_exploration.ipynb
  This notebook allows you to:
    1. *Visualize macroeconomic indicators.*
    2. *Perform PCA or explore correlations between factors.*
3. **View Outputs**
  After running the pipeline, key outputs will include:
    1. *Generated factors: Optionally saved as a processed dataset in data/processed_factors.csv.*
    2. *Portfolio performance metrics: Displayed in the terminal.*
    3. *ML model predictions: Printed or saved for further analysis*

## Project-Structure 
cross-asset-risk-parity/
├── README.md
├── requirements.txt
├── data/
│   └── sample_macro_data.csv
├── notebooks/
│   └── factor_exploration.ipynb
├── src/
│   ├── factor_synthesis.py
│   ├── adaptive_risk_budgeting.py
│   ├── ml_integration.py
│   ├── main.py
└── LICENSE


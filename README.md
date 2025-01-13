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

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/cross-asset-risk-parity.git
   cd cross-asset-risk-parity

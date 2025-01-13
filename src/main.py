import pandas as pd
import numpy as np
from factor_synthesis import factor_synthesis
from adaptive_risk_budgeting import adaptive_risk_budgeting
from ml_integration import ml_integration

def main():
    # 1. Load data
    df = pd.read_csv('data/sample_macro_data.csv', parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    
    # 2. Factor synthesis
    macro_cols = ['InterestRates', 'Inflation', 'GDPGrowth']
    df_factors = factor_synthesis(df, macro_cols, n_components=2)
    
    # 3. Combine factors with asset returns
    asset_cols = ['EquityReturns', 'BondReturns', 'FXReturns', 'CommodityReturns']
    df_combined = pd.concat([df_factors, df[asset_cols]], axis=1).dropna()
    
    # 4. Adaptive risk budgeting
    #   We'll use asset returns from df, rebalance monthly
    weights = adaptive_risk_budgeting(df[asset_cols], target_vol=0.10, lookback=3)
    
    # 5. Evaluate portfolio performance
    #   (Simple daily or monthly returns, no transaction costs)
    df_portfolio = (weights * df[asset_cols]).sum(axis=1)
    cum_returns = (1 + df_portfolio).cumprod() - 1
    
    # 6. ML integration for next-step return forecasting
    #   Example: predict next month's EquityReturns from factors
    features = df_factors
    target = df['EquityReturns'].shift(-1)  # shift so we predict future returns
    model, predictions = ml_integration(features, target)
    
    # 7. Print some results
    print("\n--- Risk Parity Portfolio Performance ---")
    final_return = cum_returns.iloc[-1] * 100
    print(f"Total Cumulative Return: {final_return:.2f}%")
    
    print("\n--- Machine Learning Predictions (Equity Returns) ---")
    print(predictions.tail(5))

if __name__ == "__main__":
    main()

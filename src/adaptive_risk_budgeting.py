import pandas as pd
import numpy as np

def adaptive_risk_budgeting(asset_returns, target_vol=0.10, lookback=30):
    """
    Dynamically rebalances asset weights to maintain a stable target volatility.

    Params:
        asset_returns (pd.DataFrame): DataFrame where each column is an asset’s returns.
        target_vol (float): Desired annualised volatility (e.g. 0.10 for 10%).
        lookback (int): Number of periods for rolling volatility estimation.

    Returns:
        weights (pd.DataFrame): Rolling weights for each asset, rebalanced each period.
    """
    # Convert target_vol from annual to monthly if data is monthly, etc.
    # For simplicity, assume 12 periods in a year
    monthly_target_vol = target_vol / np.sqrt(12)
    
    # Calculate rolling covariance
    rolling_cov = asset_returns.rolling(window=lookback).cov()
    
    # Prepare a structure to store weights
    weights_list = []
    
    for i in range(len(asset_returns)):
        if i < lookback:
            # Not enough data for rolling covariance
            weights_list.append([np.nan]*asset_returns.shape[1])
            continue
        
        # Extract the covariance matrix for the current window
        cov_matrix = rolling_cov.iloc[i*asset_returns.shape[1] : (i+1)*asset_returns.shape[1]]
        cov_matrix = cov_matrix.values.reshape(asset_returns.shape[1], asset_returns.shape[1])
        
        # Simple inverse-variance weighting
        inv_var = np.linalg.inv(cov_matrix).dot(np.ones(asset_returns.shape[1]))
        w = inv_var / np.sum(inv_var)
        
        # Scale to meet target volatility
        portfolio_vol = np.sqrt(w.T @ cov_matrix @ w)
        scale_factor = monthly_target_vol / portfolio_vol
        w_scaled = w * scale_factor
        
        weights_list.append(w_scaled)
    
    weights = pd.DataFrame(weights_list, index=asset_returns.index, columns=asset_returns.columns)
    return weights

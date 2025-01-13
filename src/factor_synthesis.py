import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def factor_synthesis(df, macro_cols, n_components=2):
    """
    Identifies key macro factors using PCA or correlation-based approach.

    Params:
        df (pd.DataFrame): DataFrame with macro columns and date index.
        macro_cols (list): Columns for macro factors.
        n_components (int): Number of PCA components.

    Returns:
        df_factors (pd.DataFrame): DataFrame with extracted factor columns.
    """
    # Drop missing rows
    data = df[macro_cols].dropna()
    
    # Standardise
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    # PCA
    pca = PCA(n_components=n_components)
    principal = pca.fit_transform(data_scaled)
    
    # Construct factor DataFrame
    factor_cols = [f'Factor{i+1}' for i in range(n_components)]
    df_factors = pd.DataFrame(principal, index=data.index, columns=factor_cols)
    
    explained_var = pca.explained_variance_ratio_.sum()
    print(f'[Factor Synthesis] PCA explained variance: {explained_var * 100:.2f}%')
    
    return df_factors

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def ml_integration(features, target, train_ratio=0.7, n_estimators=100):
    """
    Trains a random forest to forecast asset returns.

    Params:
        features (pd.DataFrame): Feature matrix (e.g. macro factors + historical returns).
        target (pd.Series): Target variable (e.g. future returns).
        train_ratio (float): Train/test split ratio.
        n_estimators (int): Number of trees in the random forest.

    Returns:
        model (RandomForestRegressor): Trained model.
        predictions (pd.Series): Out-of-sample predictions.
    """
    # Align data
    data = pd.concat([features, target], axis=1).dropna()
    X = data[features.columns]
    y = data[target.name]
    
    split = int(len(data)*train_ratio)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]
    
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    predictions = pd.Series(preds, index=y_test.index, name='Predicted')
    
    return model, predictions

"""Train a RandomForest regression model and save it to disk.

This module loads the dataset from `DATA_FILE_PATH`, builds preprocessing
pipelines for numeric and categorical features, trains a scikit-learn
`Pipeline` containing a `ColumnTransformer` and `RandomForestRegressor`,
and persists the trained model to `MODEL_PATH`.
"""

import os

# Third-party libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Project constants (paths)
from training.train_utils import MODEL_PATH, DATA_FILE_PATH, MODEL_DIR


# -----------------------------
# Data loading and basic cleanup
# -----------------------------
# Read CSV, remove duplicate rows and unused identifier columns
df = pd.read_csv(DATA_FILE_PATH).drop_duplicates().drop(['name', 'model', 'edition'], axis=1)

# Separate features and target
X = df.drop('selling_price', axis=1)
y = df['selling_price']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# -----------------------------
# Column type selection
# -----------------------------
# Numeric columns will be imputed and scaled; categorical columns will be
# imputed and one-hot encoded.
num_col = X_train.select_dtypes(include='number').columns.tolist()
cat_col = X_train.select_dtypes(include='object').columns.tolist()


# -----------------------------
# Preprocessing pipelines
# -----------------------------
# Numeric pipeline: median imputation followed by standard scaling
num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categorical pipeline: fill missing with a constant token and one-hot encode.
# `handle_unknown='ignore'` ensures unseen categories at transform time don't error.
cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])


# Combine numeric and categorical pipelines into a single preprocessor
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipe, num_col),
    ('cat', cat_pipe, cat_col)
])


# -----------------------------
# Model setup and training
# -----------------------------
# Define the regressor and wrap preprocessing + model into a Pipeline so that
# the entire object can be saved and later used for prediction with raw inputs.
regressor = RandomForestRegressor(n_estimators=100, random_state=42)

rf_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', regressor)
])

# Train the pipeline on the training data
rf_model.fit(X_train, y_train)


# -----------------------------
# Persist the trained model
# -----------------------------
# Ensure model directory exists and dump the pipeline with joblib
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_PATH)
# data structures
import numpy as np
import pandas as pd
from tabulate import tabulate

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import yellowbrick

# machine learning
# pipeline
from sklearn.pipeline import Pipeline

# preporcessing
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, PowerTransformer, QuantileTransformer
from sklearn.preprocessing import OneHotEncoder, TargetEncoder
from category_encoders import CatBoostEncoder

# metrics
from sklearn.metrics import root_mean_squared_error, r2_score

# model
# non-ensample 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

# bagging
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor

# gradient boosting
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

# catboost
from catboost import CatBoostRegressor
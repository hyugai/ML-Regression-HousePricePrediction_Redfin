# data structures
import numpy as np
import pandas as pd
from tabulate2 import tabulate

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
from sklearn.preprocessing import StandardScaler, PowerTransformer, QuantileTransformer, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder, TargetEncoder
from category_encoders import CatBoostEncoder

# imputation
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

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
from catboost import CatBoostRegressor

# stacking
from sklearn.ensemble import StackingRegressor

# clustering
from gower import gower_matrix
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# others
import re, io, os, sys
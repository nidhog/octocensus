# -*- coding: utf-8 -*-
import time
import pandas
import random
import config
from config import file_name
from pandas import DataFrame, Series
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold as VarT

NR_TRAIN = 199523
NR_TEST  = 99762

print '=='*15,' BEGIN ','=='*15
n_features = len(config.column_names) - 1
print '> Number of features of the dataset: ', n_features

## DataFrame Manipulation Utilities
def select_row(df):
    """
    Select row at a defined position
    """
    pass

def select_rows_atrandom(df, number_of_rows = 1):
    """
    Selects random rows
    Useful for checking the data
    """
    return df.ix[random.sample(df.index, number_of_rows)]
    pass

def select_column(df, feature_name, return_list=False):
    """
    Select column given a feature name
    """
    if(return_list):
        return df[feature].tolist()
    else:
        return df[feature]
    pass
## Preprocessing functions
def deep_copy(df):
    """
    Create a deep copy of a pandas DataFrame
    """
    return DataFrame(df.values.copy(), df.index.copy(), df.columns.copy())

def data_to_numbers(df):
    d = deep_copy(df)
    for x in df:
        if isinstance(df[x].loc[0], str):
            s = Series(df[x].values.ravel()).unique()
            serie = s.tolist()
            mapping = range(len(s))
            c = df[x]
            d[x]=c.replace(serie, mapping)
    return d
### LOADING THE DATA
# load training data as a dataframe object from input file and set number of records
print '_ Loading training data...', len(config.column_names)
df_train = DataFrame(pandas.read_csv(file_name['input'], 
                                         names=config.column_names))
nr_train = len(df_train.index)
assert nr_train == NR_TRAIN
print '> Training data loaded, contains ',nr_train, ' record'


# load training data as a dataframe object from test file and set number of records
print '_ Loading test data...', len(config.column_names)
df_test  = DataFrame(pandas.read_csv(file_name['test'], 
                                         names=config.column_names))
nr_test  = len( df_test.index)
assert nr_test == NR_TEST
print '> Test data loaded, contains ',nr_test, ' record'
print '> Training data percentage: ',(float(nr_train)/(nr_train+nr_test))*100,'%'

#
print '=='*15,' INITIALIZED ','=='*15

## FEATURE SELECTION AND CLASSIFICATION
print '=='*15,' CLASSIFICATION ','=='*15
initial_feature_set = config.column_names
selected_features   = initial_feature_set
print '> Initial set of features: '
print initial_feature_set
score = {}
for feature in initial_feature_set:
    score[feature]=0
reverse_score =  {v: k for k, v in score.items()}



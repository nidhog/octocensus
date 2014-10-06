# -*- coding: utf-8 -*-
import config
from config import file_name
from pandas import DataFrame

NR_TRAIN = 199523
NR_TEST  = 99762

print '=='*15,' BEGIN ','=='*15
n_features = len(config.column_names) - 1
print '> Number of features of the dataset: ', n_features

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


# -*- coding: utf-8 -*-
## Dedupe Utilities
def compare(field1, field2):
    if field1 and field2 :
        if field1 == field2 :
            return 1
        else:
            return 0
    else :
        return npy.nan
## Useful definitions
file_name = {
            'input'   : 'data/census_income_learn.csv',
            'test'    : 'data/census_income_test.csv',
            'output'  : 'output_data.csv',
            'setting' : 'settings',
            'training': 'training_features.json'
            }

## Census data
column_names = ['age',
    'class of worker',
    'industry code',
    'occupation code',
    'education',
    'wage per hour',
    'enrolled in edu last week',
    'marital status',
    'major industry code',
    'major occupation code',
    'race',
    'hispanic origin',
    'sex',
    'member of a labor union',
    'reason for unemployment',
    'full or part time employment stat',
    'capital gains',
    'capital losses',
    'dividends from stocks',
    'tax filer stat',
    'region of previous residence',
    'state of previous residence',
    'detailed household and family stat',
    'instance weight',
    'migration code-change in msa',
    'migration code-change in reg',
    'migration code-move within reg',
    'live in this house 1 year ago',
    'migration prev res in sunbelt',
    'num persons worked for employer',
    'parents present',
    'country of birth father',
    'country of birth mother',
    'country of birth',
    'citizenship',
    '!!PR',
    'own business or self employed',
    'veteran admin',
    'veterans benefits',
    'weeks worked',
    'year',
    'goal']

import numpy as np
import pandas as pd
from pandas import DataFrame

file_path = 'msbd5001-fall2019/train.csv'
# file_path = 'msbd5001-fall2019/test.csv'
data = pd.read_csv(file_path)
print('*' * 100)
print(data)

print('*' * 100)
print('genres:')
dummies_genres = data['genres'].str.get_dummies(",") 
print(dummies_genres)

print('*' * 100)
print('categories:')
dummies_categories = data['categories'].str.get_dummies(",").drop(['Co-op'], axis=1)
print(dummies_categories)

print('*' * 100)
print('tags:')
dummies_tags = data['tags'].str.get_dummies(",")
print(dummies_tags)

print('*' * 100)
print('data:')
data = data.join(dummies_tags).join(dummies_categories).drop(['genres', 'categories', 'tags'], axis=1)
print(data)

print('*' * 100)
print('purchase date:')
purchase_date = pd.to_datetime(data['purchase_date'])
print(purchase_date)

print('*' * 100)
print('release date:')
release_date = pd.to_datetime(data['release_date'])
print(release_date)

print('*' * 100)
print(purchase_date - release_date)

print('*' * 100)
print('purchased days:')
purchased_days = (purchase_date - release_date).dt.days
data.insert(1, 'purchased_days', purchased_days)
print(data['purchased_days'])


print('*' * 100)
print('data:')
data.drop(['purchase_date', 'release_date'], axis=1, inplace=True)
data['is_free'] = data['is_free'].astype(int)
data.dropna(axis=0, how='any', inplace=True)
# print(data)
data.fillna(data.mean(), inplace=True)

data.to_csv('./msbd5001-fall2019/train1.csv')
# data.to_csv('./msbd5001-fall2019/test1.csv')
# Handling missing data
## None

import numpy as np
import pandas as pd

vals1 = np.array([1, None, 3, 4])
vals1

vals1.sum()

## NaN: Missing numerical data

vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype

vals2.sum(), vals2.min(), vals2.max()

### Ignoring NaN

np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)

## Operating on null values
data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

data[data.notnull()]

### Dropping null values

data.dropna()

df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5], [np.nan, 4, 6]])

#### Dropping rows

df.dropna()

#### Dropping columns

df.dropna(axis = 'columns')

#### Dropping only columns/rows that all values are NaN

df[3] = np.nan
df

df.dropna(axis='columns', how = 'all')

#### Dropping a minimum number

df.dropna(axis='rows', thresh = 3)

### Filling null values

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

data.fillna(0)
data.fillna(method='ffill') # forward-fill - propagate the previous value forward
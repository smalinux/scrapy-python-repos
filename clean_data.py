import pandas as pd
import numpy as np


df = pd.read_csv('./most_started.csv', squeeze=True)
df['stars'] = df['stars'].astype(str).str[:-1].astype(np.float_)
print(df['stars'])

df.to_csv('./output.csv', index=False)



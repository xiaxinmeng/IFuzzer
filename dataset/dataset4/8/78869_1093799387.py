from pandas import DataFrame
import pandas as pd

df = DataFrame({'A': [1, 2, 3],
                'B': [1., 2., 3.],
                'C': ['foo', 'bar', 'baz'],
                'D': pd.date_range('20130101', periods=3)})

print(df.agg('sum'))
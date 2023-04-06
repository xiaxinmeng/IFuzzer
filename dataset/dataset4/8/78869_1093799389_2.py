from pandas import DataFrame
import pandas as pd

df = DataFrame({'D': pd.date_range('20130101', periods=3)})

print(df.agg('sum'))
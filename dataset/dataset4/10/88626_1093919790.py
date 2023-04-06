import pandas as pd
d = {'col1': [[0.] * 25] * 2560}
df = pd.DataFrame(data=d)
df.to_parquet('data.parquet')
for j in range(15):
  table = pd.read_parquet('data.parquet')
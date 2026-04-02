from pathlib import Path
import pandas as pd

p = Path("data")
dfs = {}

for file in p.glob("*.csv"):
    name = file.stem
    dfs[name] = pd.read_csv(file)
    # print(dfs[name].info())
    # print(f"Loaded: {name} (shape: {dfs[name].shape})")
    
print(dfs["products"].head())
print(dfs["products"].isna().sum())
print(dfs["products"].duplicated().sum())
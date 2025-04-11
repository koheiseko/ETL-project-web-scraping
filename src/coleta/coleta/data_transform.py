import pandas as pd
from numpy import nan

dt = pd.read_csv("../data.csv")

dt['desconto'] = dt['old-money'] - dt['new-money']

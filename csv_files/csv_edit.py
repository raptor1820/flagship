import pandas as pd
nationalParties = pd.read_csv(r'nationalparties.csv')
regionalParties  = pd.read_csv(r'regionalparties.csv')

nationalParties.replace("-","0")
regionalParties.replace("-","0")

nationalParties.fillna(0)
regionalParties.fillna(0)




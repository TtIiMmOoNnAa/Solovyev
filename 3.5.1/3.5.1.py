import pandas as pd
import sqlite3

url = "kurs_k_rub_ves_api.csv"
dataframe = pd.read_csv(url)
u1 = "kurs_po_CB.db"
# conect k bd
baz = sqlite3.connect(u1)
cur = baz.cursor()
naz = "kurs_k_rub"
# dan v bd
dataframe.to_sql(name=naz, con=baz, if_exists='replace', index=False)
baz.commit()
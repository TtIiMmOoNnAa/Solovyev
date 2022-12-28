import math
import pandas as pd
from statistics import mean
import sqlite3

dl_kurs = {"BYR": 1,
           "EUR": 2,
           "KZT": 3,
           "UAH": 4,
           "USD": 5}


# ищем зарплаты
def formirovan_zarp(s_f, s_t, kurs_v, date):
    b1 = date[1]
    b2 = date[0]
    year_month = b1 + "/" + b2
    k_v = 0
    val = ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]
    if (kurs_v == kurs_v) and kurs_v in val and "RUR" != kurs_v:
        a1, a2 = "BYN", "BYR"
        kurs_v.replace(a1, a2)
        zapros1 = "SELECT * FROM kurs_k_rub WHERE date == :year_month"
        cur.execute(zapros1, {"year_month": year_month})
        k_v = cur.fetchall()[0][dl_kurs[kurs_v]]
    elif "RUR" == kurs_v:
        k_v = 1
    if not (math.isnan(s_t)) and math.isnan(s_f):
        rez1 = k_v * s_t
        return rez1
    elif math.isnan(s_t) and not (math.isnan(s_f)):
        rez2 = s_f * k_v
        return rez2
    elif not ((math.isnan(s_f)) and (math.isnan(s_t))):
        rez3 = mean([s_f, s_t]) * k_v
        return rez3


url1 = "vacancies_dif_currencies.csv"
df = pd.read_csv(url1)
bd1 = "kurs_po_CB.db"
con = sqlite3.connect(bd1)
cur = con.cursor()


# колонка год месяц
def form_kolon_vremy():
    rez = lambda date: date[:7]
    return rez


p = "published_at"
df[p] = df[p].apply(form_kolon_vremy())


# колонка год
def form_god():
    rez = lambda date: date[:4]
    return rez


r_a1 = "years"
r_a2 = "published_at"
df[r_a1] = df[r_a2].apply(form_god())


# ищем зарплаты
def scit_zarplat_vac():
    a1, a2, a3, a4 = "salary_from", "salary_to", "salary_currency", "published_at"
    rez = lambda stroka: formirovan_zarp(stroka[a1], stroka[a2], stroka[a3], stroka[a4][:7].split("-"))
    return rez


ss = "salary"
df.insert(1, ss, df.apply(scit_zarplat_vac(), axis=1))
udol = ["salary_from", "salary_to", "salary_currency"]
df.drop(udol, axis=1, inplace=True)

bd2 = 'New_vac.db'
connect = sqlite3.connect(bd2)
cursor = con.cursor()
url2 = "New_vac_currencies"
df.to_sql(name=url2, con=connect, if_exists='replace', index=False)
connect.commit()

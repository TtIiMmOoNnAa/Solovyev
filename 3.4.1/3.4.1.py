import pandas as pd
import math
from statistics import mean

u = "expand_frame_repr"
pd.set_option(u, False)
url1 = "vacancies_dif_currencies.csv"
dataframe = pd.read_csv(url1)
url2 = "kurs_k_rub_ves_api.csv"
dataframe_d = pd.read_csv(url2)

def delarm_kolon_salary():
    a1, a2, a3, a4 = "salary_from", "salary_to", "salary_currency", "published_at"
    rez = lambda stroka: formirov_zarplat(stroka[a1], stroka[a2], stroka[a3], stroka[a4][:7].split("-"))
    return rez


def formirov_zarplat(z_f, z_t, z_kurs, date):
    b1 = date[1]
    b2 = date[0]
    r1 = b1 + "/" + b2
    date = r1
    znach = 0
    k = ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]
    if (z_kurs == z_kurs) and z_kurs in k and "RUR" != z_kurs:
        d1, d2 = "BYN", "BYR"
        z_kurs.replace(d1, d2)
        d = "date"
        dataframe_str = dataframe_d.loc[date == dataframe_d[d]]
        znach = dataframe_str[z_kurs].values[0]
    elif "RUR" == z_kurs:
        znach = 1
    if not (math.isnan(z_t)) and math.isnan(z_f):
        rez3 = znach * z_t
        return rez3
    elif math.isnan(z_t) and not (math.isnan(z_f)):
        rez2 = znach * z_f
        return rez2
    elif not ((math.isnan(z_f)) and (math.isnan(z_t))):
        rez1 = znach * mean([z_f, z_t])
        return rez1


ss = "salary"
dataframe[ss] = dataframe.apply(delarm_kolon_salary(), axis=1)
n_u = "New_vacancy.csv"
dataframe[:100].to_csv(n_u, index=False)
print(dataframe[:100])

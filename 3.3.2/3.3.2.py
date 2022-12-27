import math
from statistics import mean
import pandas as pd

pd.set_option("expand_frame_repr", False)
s = "Введите название файла: "
file = input(s)
datarame = pd.read_csv(file)
u = "kurs_k_rub_ves_api.csv"
kurs_po_api = pd.read_csv(u)


def proverka(zarp_f, zarp_p, kurs_v):
    f_n = math.isnan(zarp_f)
    t_n = math.isnan(zarp_p)

    if f_n and not t_n:
        r = zarp_p * kurs_v
        return r
    elif not f_n and t_n:
        r = zarp_f * kurs_v
        return r
    elif not f_n and not t_n:
        r = mean([zarp_f, zarp_p]) * kurs_v
        return r


def perev_zarp(z_f, z_p, v, published_at):
    published_at = published_at[1] + "/" + published_at[0]
    k_v = 0
    v1 = "RUR"
    if (v == v) and v1 != v:
        m = ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]
        if v in m:
            v2, v3 = "BYR", "BYN"
            if v == v3:
                v = v2
            else:
                v = v
            api_str = kurs_po_api.loc[kurs_po_api["date"] == published_at]
            k_v = api_str[v].values[0]
    elif v == "RUR":
        k_v = 1
    rez = proverka(z_f, z_p, k_v)

    return rez


a, b, c, d, e = "salary", "salary_from", "salary_to", "salary_currency", "published_at"


def zapolndata():
    return lambda stroka: perev_zarp(stroka[b], stroka[c], stroka[d], stroka[e][:7].split("-"))


datarame[a] = datarame.apply(zapolndata(), axis=1)

u1 = "vacancies_dif_currencies_100.csv"
datarame[:100].to_csv(u1, index=False)

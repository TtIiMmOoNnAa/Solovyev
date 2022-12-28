import pandas as pd
import requests

interval = list()
b1, b2 = 1, 23
for num in range(b1, b2):
    s1 = str(num)
    a1 = s1.zfill(2)
    s2 = str(num + 1)
    a2 = s2.zfill(2)
    interval.append(f"https://api.hh.ru/vacancies?specialization=1&date_from=2022-12-27T{a1}:00:00&date_to=2022-12-27T{a2}:00:00&")
col = ["name",
       "salary_from",
       "salary_to",
       "salary_currency",
       "area_name",
       "published_at"]
dataframe = pd.DataFrame(columns=col)
# Находим количество страниц, идем по каждой странице, берем все вакансии на странице и идём по всем вакансиям
for u in interval:
    r1 = requests.get(u).json()
    js_v_pag = r1
    ss1 = "pages"
    dl1 = js_v_pag[ss1] + 1
    for p in range(dl1):
        r_s = "per_page"
        g1 = js_v_pag[r_s]
        if 100 > g1:
            r_s1 = 'page'
            res1 = {r_s1: p}
            par = res1
        else:
            r_s1 = 'per_page'
            r_s2 = 'page'
            res1 = {r_s1: '100',
                      r_s2: p}
            par = res1
        s_r = "items"
        rez1 = requests.get(u, params=par).json()[s_r]
        items = rez1
        for znach in items:
            try:
                dlin = len(dataframe)
                dataframe.loc[dlin] = [znach["name"],
                                       znach["salary"]["from"],
                                       znach["salary"]["to"],
                                       znach["salary"]["currency"],
                                       znach["area"]["name"],
                                       znach["published_at"]]
            except TypeError:
                continue
ss = "vac_hunter_2022_12_27.csv"
dataframe.to_csv(ss, index=False)
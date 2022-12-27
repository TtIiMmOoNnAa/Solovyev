import pandas as pd
import requests

def obrabotka_d(danii, sim):
    return float(obr_d1(danii, sim)) / \
           float(obr_d2(danii, sim))


def obr_d2(danii, sim):
    return danii.loc[danii["CharCode"] == sim]["Nominal"].values[0]


def obr_d1(danii, sim):
    return danii.loc[danii["CharCode"] == sim]["Value"].values[0].replace(',', ".")


def obrabotka_dataframe(date):
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=15/{date}d=1"
    r = requests.get(url)
    d_x = pd.read_xml(r.text)
    val = ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]
    dataframe_f = d_x.loc[d_x['CharCode'].isin(val)]
    a = dataframe_f.loc[dataframe_f["CharCode"].isin(["BYR", "BYN"])]["Value"].values[0].replace(',', ".")
    b = dataframe_f.loc[dataframe_f["CharCode"].isin(["BYR", "BYN"])]["Nominal"].values[0]
    BYR = float(a) / \
          float(b)
    s1, s2, s3, s4 = "EUR", "KZT", "UAH", "USD"
    EUR = (obrabotka_d(dataframe_f, s1))
    KZT = (obrabotka_d(dataframe_f, s2))
    UAH = (obrabotka_d(dataframe_f, s3))
    USD = (obrabotka_d(dataframe_f, s4))
    rez = [date, BYR, EUR, KZT, UAH, USD]
    dl = len(kurs_val_k_rub_f)
    kurs_val_k_rub_f.loc[dl] = rez

pd.set_option("expand_frame_repr", False)
file = input("Введите название файла: ")
dataframe = pd.read_csv(file)
print(dataframe.groupby("salary_currency").size())
ss = "salary_currency"
dataframe_kur = dataframe[ss].value_counts()
dataframe_kur = dataframe_kur.apply(lambda kurs: kurs if kurs >= 5000 else False)
ss1 = "published_at"
start_date = dataframe[ss1].min()[:7].split("-")
final_date = dataframe[ss1].max()[:7].split("-")
rr = ["date", "BYR", "USD", "EUR", "KZT", "UAH"]
kurs_val_k_rub_f = pd.DataFrame(columns=rr)
a1, a2 = 2003, 2023
for god in range(a1, a2):

    if 2022 == god:
        b1, b2 = 1, (int(final_date[1]) + 1)
        for mesyc in range(b1, b2):
            if 1 <= mesyc <= 9:
                sss = f"0{mesyc}/{god}"
                obrabotka_dataframe(sss)
            else:
                sss = f"{mesyc}/{god}"
                obrabotka_dataframe(sss)
    else:
        b1, b2 = int(start_date[1]), 13
        for mesyc in range(b1, b2):
            if 1 <= mesyc <= 9:
                sss = f"0{mesyc}/{god}"
                obrabotka_dataframe(sss)
            else:
                sss = f"{mesyc}/{god}"
                obrabotka_dataframe(sss)
kurs_val_k_rub_f.to_csv("kurs_k_rub_ves_api.csv", index=False)
print(kurs_val_k_rub_f["salary_currency"].value_counts())


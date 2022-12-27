import pandas as pd

# начало
pd.set_option("expand_frame_repr", False)
s1 = "Введите название файла: "
file_name = input(s1)
dataframe = pd.read_csv(file_name)


# делаем правильные даты
def form_data():
    rez1 = lambda date: int(".".join(date[:4].split("-")))
    return rez1


s_g, s_p = "years", "published_at"
dataframe[s_g] = dataframe[s_p].apply(form_data())
s_y = "years"
goda = dataframe[s_y].unique()


# список столбцов название
def list_naz_stol():
    rez = ["name",
           "salary_from",
           "salary_to",
           "salary_currency",
           "area_name",
           "published_at"]
    return rez


# делаем файлы csv
for god in goda:
    s = "years"
    data_to_insert = dataframe[god == dataframe[s]]
    r_s1 = f"csv_f\\god{god}.csv"
    data_to_insert[list_naz_stol()].to_csv(r_s1, index=False)
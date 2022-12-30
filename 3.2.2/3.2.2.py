import time
import pandas as pd
from multiprocessing import Process, Queue

slovar = list()


# Функция для мультипроцессинга
def start_processes(v_n, god, que):
    ur1 = f'csv_f\\god{god}.csv'
    razdel_csv = pd.read_csv(ur1)
    # применить вычисление построчно
    r1 = ['salary_from', 'salary_to']
    s1 = 'salary'
    res1 = razdel_csv.loc[:, r1]
    razdel_csv.loc[:, s1] = razdel_csv.loc[:, r1].mean(axis=1)
    # вакансии по заданному названию профессии
    r2 = razdel_csv["name"].str.contains(v_n)
    res2 = razdel_csv[r2]
    p_dataframe = res2
    s_b_g, v_b_g, i_v_z, i_v_kol = {god: []}, {god: 0}, {god: []}, {god: 0}
    rez1 = razdel_csv['salary'].mean()
    rez_1 = int(rez1)
    s_b_g[god] = rez_1
    rez2 = len(razdel_csv)
    v_b_g[god] = rez2
    rez3 = p_dataframe['salary'].mean()
    rez_3 = int(rez3)
    i_v_z[god] = rez_3
    rez4 = len(p_dataframe)
    i_v_kol[god] = rez4
    rez5 = [s_b_g, v_b_g, i_v_z, i_v_kol]
    d_list = rez5
    que.put(d_list)





def vivod_rezult():
    print("Динамика уровня зарплат по годам:", sortirovka_slovar(s_b_y))
    print("Динамика количества вакансий по годам:", sortirovka_slovar(v_b_y))
    print("Динамика уровня зарплат по годам для выбранной профессии:", sortirovka_slovar(i_v_sa))
    print("Динамика количества вакансий по годам для выбранной профессии:", sortirovka_slovar(i_v_kole))
    print("Уровень зарплат по городам (в порядке убывания):", sortirovka_gorodov(salaries_areas))
    print("Доля вакансий по городам (в порядке убывания):", sortirovka_gorodov(vacancies_areas))


if __name__ == "__main__":
    tic = time.perf_counter()


    class MakeCvs:
        def __init__(self, file_name):
            self.dataframe = pd.read_csv(file_name)

            self.dataframe["years"] = self.dataframe["published_at"].apply(self.sostavl_vremy())
            self.years = list(self.dataframe["years"].unique())

            for year in self.years:
                data = self.dataframe[self.dataframe["years"] == year]
                rezul = ["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]
                url2 = f"csv_f\\god{year}.csv"
                #rr = data[rezul]
                data[rezul].to_csv(url2, index=False)

        def sostavl_vremy(self):
            return lambda date: int(".".join(date[:4].split("-")))


    def sortirovka_gorodov(slovar):
        r = sorted(slovar.items(), key=slovar_po_znach(), reverse=True)
        sor_t = r[:10]
        fin_d = {kluch: znach for kluch, znach in sor_t}
        rez = fin_d
        return rez


    def slovar_po_znach():
        return lambda item: item[1]


    def sortirovka_slovar(slovar):
        n_slov = dict()
        prpogon = sorted(slovar)
        for kluch in prpogon:
            rez = slovar[kluch]
            n_slov[kluch] = rez
        return n_slov


    class Input:
        def __init__(self):
            self.file_name = input("Введите название файла: ")
            self.vacancy_name = input("Введите название профессии: ")

    uu = "expand_frame_repr"
    pd.set_option(uu, False)
    vse_dan = Input()
    f, v = vse_dan.file_name, vse_dan.vacancy_name
    obr_c = MakeCvs(f)
    dataf = obr_c.dataframe
    goda = obr_c.years
    dataf["published_at"] = dataf["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
    rez1 = ['salary_from', 'salary_to']
    rr1 = dataf.loc[:, rez1]
    dataf['salary'] = dataf.loc[:, rez1].mean(axis=1)
    dl1 = len(dataf)
    vacancies = dataf
    #rr2 = dataf.groupby("area_name")['area_name']
    dataf["count"] = dataf.groupby("area_name")['area_name'].transform("count")
    doly_n = dataf[dataf['count'] >= 0.01 * vacancies]
    gords = list(doly_n["area_name"].unique())
    s_b_y, v_b_y, i_v_sa, i_v_kole, salaries_areas, vacancies_areas \
        = {}, {}, {}, {}, {}, {}
    for city in gords:
        df_s = doly_n[doly_n['area_name'] == city]
        salaries_areas[city] = int(df_s['salary'].mean())
        vacancies_areas[city] = round(len(df_s) / len(dataf), 4)

    q = Queue()
    processes = []
    # Начинаем все процессы
    for y in goda:
        p = Process(target=start_processes, args=(v, y, q))
        processes.append(p)
        p.start()

    # Завершаем все процессы
    for p in processes:
        dicts_list = q.get()
        s_b_y.update(dicts_list[0])
        v_b_y.update(dicts_list[1])
        i_v_sa.update(dicts_list[2])
        i_v_kole.update(dicts_list[3])
        p.join()

    vivod_rezult()
    toc = time.perf_counter()
    print(f"Вычисление заня\ло {toc - tic:0.4f} секунд")

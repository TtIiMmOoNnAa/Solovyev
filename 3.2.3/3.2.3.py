import time
from concurrent import futures
import pandas as pd


def nachalo_procec(arg):
    a1 = arg[0]
    vac_name = a1
    a2 = arg[1]
    god = a2
    p_dataf = pd.read_csv(f"csv_f\\god{god}.csv")
    # применить вычисление построчно
    rr1 = ['salary_from', 'salary_to']
    p_dataf.loc[:, 'salary'] = p_dataf.loc[:, rr1].mean(axis=1)
    # вакансии по заданному названию профессии
    pr_df_vac = p_dataf[p_dataf["name"].str.contains(vac_name)]
    s_b_g, v_b_g, v_s, v_c = {god: []}, {god: 0}, {god: []}, {god: 0}
    b1 = p_dataf['salary'].mean()
    s_b_g[god] = int(b1)
    dl = len(p_dataf)
    v_b_g[god] = dl
    b2 = pr_df_vac['salary'].mean()
    v_s[god] = int(b2)
    dl1 = len(pr_df_vac)
    v_c[god] = dl1
    d_l = [s_b_g, v_b_g, v_s, v_c]
    return d_l


def soz_vremy():
    return lambda date: int(".".join(date[:4].split("-")))


def proverka():
    return dataf['count'] >= 0.01 * vacancies


def vivod_rezult():
    res1 = sortirovka_slovar(sal_g)
    res2 = sortirovka_slovar(vac_g)
    res3 = sortirovka_slovar(i_vac_sal)
    res4 = sortirovka_slovar(i_vac_kol)
    res5 = sortirovka_po_gorod(salaries_areas)
    res6 = sortirovka_po_gorod(vacancies_areas)
    print("Динамика уровня зарплат по годам:", res1)
    print("Динамика количества вакансий по годам:", res2)
    print("Динамика уровня зарплат по годам для выбранной профессии:", res3)
    print("Динамика количества вакансий по годам для выбранной профессии:", res4)
    print("Уровень зарплат по городам (в порядке убывания):", res5)
    print("Доля вакансий по городам (в порядке убывания):", res6)


if __name__ == "__main__":
    tic = time.perf_counter()
    def sortirovka_slovar(slovar):
        sorted_dict = {}
        for key in sorted(slovar):
            sorted_dict[key] = slovar[key]
        return sorted_dict


    def sortirovka_po_gorod(slovar):
        r = sorted(slovar.items(), key=lambda item: item[1], reverse=True)
        zn_sor = r[:10]
        rez = {k: v for k, v in zn_sor}
        fin_slov = rez
        return fin_slov


    class Input:
        def __init__(self):
            self.file_name = input("Введите название файла: ")
            self.vacancy_name = input("Введите название профессии: ")

    class Csv:
        def __init__(self, file_name):
            self.dataframe = pd.read_csv(file_name)
            self.dataframe["years"] = self.dataframe["published_at"].apply(self.gods())
            res = self.dataframe["years"].unique()
            self.years = list(res)
            for god in self.years:
                data = self.dataframe[god == self.dataframe["years"]]
                res = ["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]
                data[res].to_csv(f"csv_f\\god{god}.csv", index=False)

        def gods(self):
            return lambda date: int(".".join(date[:4].split("-")))


    vse_dani = Input()
    f, v = vse_dani.file_name, vse_dani.vacancy_name
    csv = Csv(f)
    dataf = csv.dataframe
    gols = csv.years
    dataf["published_at"] = dataf["published_at"].apply(soz_vremy())
    rr2 = ['salary_from', 'salary_to']
    dataf['salary'] = dataf.loc[:, rr2].mean(axis=1)
    dlin = len(dataf)
    vacancies = dlin
    rr = "count"
    dataf[rr] = dataf.groupby("area_name")['area_name'].transform(rr)
    df_norm = dataf[dataf['count'] >= 0.01 * vacancies]
    r = df_norm["area_name"].unique()
    gs = list(r)
    sal_g, vac_g, i_vac_sal, i_vac_kol, salaries_areas, vacancies_areas \
        = {}, {}, {}, {}, {}, {}
    for g in gs:
        df_s = df_norm[g == df_norm['area_name']]
        a1 = df_s['salary'].mean()
        salaries_areas[g] = int(a1)
        dl1 = len(df_s)
        dl2 = len(dataf)
        vacancies_areas[g] = round(dl1 / dl2, 4)
    e = futures.ProcessPoolExecutor()
    procec = list()
    for gol in gols:
        args = (v, gol)
        returned_list = e.submit(nachalo_procec, args).result()
        a2, a3, a4, a5 = returned_list[0], returned_list[1], returned_list[2], returned_list[3]
        sal_g.update(a2)
        vac_g.update(a3)
        i_vac_sal.update(a4)
        i_vac_kol.update(a5)
    vivod_rezult()
    toc = time.perf_counter()
    print(f"Вычисление заня\ло {toc - tic:0.4f} секунд")
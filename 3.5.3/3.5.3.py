import sqlite3
import pandas as pd


# вывод результата
def vivid_result():
    print("Динамика уровня зарплат по годам:", z_po_g)
    print("Динамика количества вакансий по годам:", v_po_g)
    print("Динамика уровня зарплат по годам для выбранной профессии:", d_z_po_g)
    print("Динамика количества вакансий по годам для выбранной профессии:", d_k_vac_po_g)
    print("Уровень зарплат по городам (в порядке убывания):", salaries_areas)
    print("Доля вакансий по городам (в порядке убывания):", vacancies_areas)


# заполнение больше 1%
def zapol_bol_procent():
    return 0.01 * razmer_baza <= z_po_gorod["COUNT(area_name)"]


# сортируем все по условию задачи
def sortirovachn_method(slovar):
    sor_d = sorted(slovar.items(), key=lambda item: item[1], reverse=True)
    sor = sor_d[:10]
    rez = {kluch: znach for kluch, znach in sor}
    fin_sor_d = rez
    return fin_sor_d


# счет доли вакансий
def schet_doly():
    return dol_po_gor["COUNT(area_name)"] / razmer_baza * 100


vvod1 = "База данных по которой проводится анализ: New_vac.db"
print(vvod1)
n_v = "Введите название профессии: "
profession = input(n_v)
r_f = f"%{profession}%"
profession = r_f
bd = "New_vac.db"
con = sqlite3.connect(bd)
cur = con.cursor()
zapros0 = "SELECT COUNT(*) FROM New_vac_currencies"
a1 = "COUNT(*)"
razmer_baza = pd.read_sql(zapros0, con).to_dict()
razmer_baza = razmer_baza[a1][0]

# Динамика уровня зарплат по годам
zapros1 = "SELECT years, ROUND(AVG(salary)) FROM New_vac_currencies GROUP BY years"
zarp_po_god = pd.read_sql(zapros1, con)
res1 = ["years", "ROUND(AVG(salary))"]
a0, a2 = "split", "data"
r0 = zarp_po_god[res1].to_dict(a0)[a2]
rez1 = dict(r0)
z_po_g = rez1

# Динамика количества вакансий по годам
zapros2 = "SELECT years, COUNT(name) FROM New_vac_currencies GROUP BY years"
vac_po_god = pd.read_sql(zapros2, con)
res2 = ["years", "COUNT(name)"]
r1 = vac_po_god[res2].to_dict(a0)[a2]
rez2 = dict(r1)
v_po_g = rez2

# Динамика уровня зарплат по годам для выбранной профессии
zapros3 = "SELECT years, ROUND(AVG(salary)) FROM New_vac_currencies WHERE name LIKE :vac GROUP BY years"
b1 = [profession]
vbran_p_zarp_po_g = pd.read_sql(zapros3, con, params=b1)
res3 = ["years", "ROUND(AVG(salary))"]
r2 = vbran_p_zarp_po_g[res3].to_dict(a0)[a2]
rez3 = dict(r2)
d_z_po_g = rez3

# Динамика количества вакансий по годам для выбранной профессии
zapros4 = "SELECT years, COUNT(name) FROM New_vac_currencies encies WHERE name LIKE :vac GROUP BY years"
kol_vac_po_vsbr = pd.read_sql(zapros4, con, params=b1)
res4 = ["years", "COUNT(name)"]
r3 = kol_vac_po_vsbr[res4].to_dict(a0)[a2]
rez4 = dict(r3)
d_k_vac_po_g = rez4

# Уровень зарплат по городам (в порядке убывания)
zapros5 = "SELECT area_name, ROUND(AVG(salary)), COUNT(area_name) FROM New_vac_currencies GROUP BY area_name ORDER BY COUNT(area_name) DESC "
z_po_gorod = pd.read_sql(zapros5, con)
z_po_gorod = z_po_gorod[zapol_bol_procent()]
res5 = ["area_name", "ROUND(AVG(salary))"]
r4 = z_po_gorod[res5].to_dict(a0)[a2]
rez5 = dict(r4)
salaries_areas = rez5
salaries_areas = sortirovachn_method(salaries_areas)

# Доля вакансий по городам (в порядке убывания)
zapros6 = "SELECT area_name, COUNT(area_name) FROM New_vac_currencies GROUP BY area_name ORDER BY COUNT(area_name) DESC LIMIT 10"
dol_po_gor = pd.read_sql(zapros6, con)
b4 = "COUNT(area_name)"
r = round(schet_doly(), 2)
dol_po_gor[b4] = r
res6 = ["area_name", 'COUNT(area_name)']
r6 = dol_po_gor[res6].to_dict(a0)[a2]
rez6 = dict(r6)
vacancies_areas = rez6

vivid_result()
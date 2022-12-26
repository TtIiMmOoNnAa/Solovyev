import os
import re
import cProfile
import csv
from datetime import datetime


def ochhistka(stroka):
    stroka = re.sub('<.*?>', '', stroka)
    stroka = stroka.replace("\r\n", "\n")
    r_f = [' '.join(slovo.split()) for slovo in stroka.split('\n')]
    dl = len(r_f)
    if 1 == dl:
        return r_f[0]
    else:
        return r_f


class DataSet:
    def __init__(self, file_name):
        if 0 == os.stat(file_name).st_size:
            s3 = "Пустой файл"
            oshibki_vse(s3)
        self.vacancies = [row for row in csv.reader(open(file_name, encoding="utf_8_sig"))]
        self.shapka = self.vacancies[0]
        self.g_f = [s for s in self.vacancies[1:] if len(self.shapka) == len(s) and 0 == s.count('')]
        d = len(self.g_f)
        if 0 == d:
            s3 = 'Нет данных'
            oshibki_vse(s3)


def oshibki_vse(oshibk):
    r = oshibk
    print(r)
    exit(0)


class Input:
    def __init__(self):
        s1 = 'Введите название файла: '
        self.file_name = input(s1)
        s2 = 'Введите название профессии: '
        self.vacancy_name = input(s2)


kurs_k_rub = {
    "Манаты": 35.68,
    "Белорусские рубли": 23.91,
    "Евро": 59.90,
    "Грузинский лари": 21.74,
    "Киргизский сом": 0.76,
    "Тенге": 0.13,
    "Рубли": 1,
    "Гривны": 1.64,
    "Доллары": 60.66,
    "Узбекский сум": 0.0055,
}


class Vacancy:
    published_at = list()

    @staticmethod
    def profilirov_vremy(list_d):
        r_a = datetime.strptime(list_d, '%Y-%m-%dT%H:%M:%S%z').strftime("%Y")
        res = int(r_a)
        n_d = res
        #r_a2 = ".".join(list_d[:4].split("-"))
        #res2 = int(r_a2)
        # n_d = res2
        #p = list_d[:19].split('T')
        #list_d = p[0].split('-')
        #n_d = int(list_d[0])
        return n_d

    def __init__(self, v_v):
        for on_v in v_v:
            a = on_v.items()
            for kluch, znach in a:
                if 'published_at' == kluch:
                    self.published_at.append(self.profilirov_vremy(znach))


perev_ru = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум",
}

osn_d = Input()
dataset = DataSet(osn_d.file_name)
shapka = dataset.shapka
obra_vac = dataset.g_f
vse = list()
for o_v in obra_vac:
    a = map(ochhistka, o_v)
    b = zip(shapka, a)
    c = dict(b)
    vse.append(c)
u = 'Vacancy(vse)'
cProfile.run(u)

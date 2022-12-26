import re
from unittest import TestCase
import task_testirovan

file_name = "vacancies.csv"
vac_name = "Аналитик"
dataset = task_testirovan.DataSet(file_name)
shap = dataset.shapka


class DataSetTests(TestCase):
    def test_nul_dlina(self):
        nomar = 0
        for znach in self.dataset.obrabot_vse_vac:
            if "" == znach:
                nomar = nomar + 1
        self.assertEqual(0, nomar)

    ur = "vacancies.csv"
    dataset = task_testirovan.DataSet(ur)


class VacancyTest(TestCase):
    isprav_vsc1 = dataset.obrabot_vse_vac[0]
    isprav_vac2 = {"name": "Программист",
                   "salary_from": "100.0",
                   "salary_to": "5000.0",
                   "salary_currency": "USD",
                   "area_name": "тута",
                   "published_at": "2022-01-12T14:12:06-0500"}

    def test_salary_published(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.published_at, 2007)

    def test_salary_type(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(type(odn_v.salary).__name__, "int")

    @staticmethod
    def ochistcka_strok(stroka):
        stroka = re.sub('<.*?>', '', stroka)
        stroka = stroka.replace("\r\n", "\n")
        res = [' '.join(word.split()) for word in stroka.split('\n')]
        dl = len(res)
        if 1 == dl:
            return res[0]
        else:
            return res

    def test_salary_from_type(self):
        vac = task_testirovan.Vacancy(self.isprav_vac2)
        self.assertEqual(type(vac.salary_from).__name__, "str")

    def test_salary_from(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.salary_from, "35 000")

    def test_salary_to(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.salary_to, "45 000")

    def test_salary_name(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.name, "IT аналитик")

    def test_salary_currency(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.salary_currency, "Рубли")

    def test_salary_area_name(self):
        a = map(self.ochistcka_strok, self.isprav_vsc1)
        b = zip(shap, a)
        r = dict(b)
        odn_v = task_testirovan.Vacancy(r)
        self.assertEqual(odn_v.area_name, "Санкт-Петербург")


class ResultStaticTest(TestCase):
    def test_prav_slovar(self):
        self.assertEqual(self.f_rez.sortirovk_slovar(self.kurs_k_rub), self.prav_kur)

    f_rez = task_testirovan.FinalStatisticka()
    prav_kur = {"Доллары": 60.66,
                "Евро": 59.90,
                "Манаты": 35.68,
                "Белорусские рубли": 23.91,
                "Грузинский лари": 21.74,
                "Гривны": 1.64,
                "Рубли": 1,
                "Киргизский сом": 0.76,
                "Тенге": 0.13,
                "Узбекский сум": 0.0055, }
    kurs_k_rub = {"Манаты": 35.68,
                  "Белорусские рубли": 23.91,
                  "Евро": 59.90,
                  "Грузинский лари": 21.74,
                  "Киргизский сом": 0.76,
                  "Тенге": 0.13, "Рубли": 1,
                  "Гривны": 1.64,
                  "Доллары": 60.66,
                  "Узбекский сум": 0.0055, }

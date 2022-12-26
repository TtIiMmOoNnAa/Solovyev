SOLOVYEV

2.3.2

Проверка доктестов

![](png/z2.3.21.png)

Проверка юниттестов

![](png/z2.3.22.png)

2.3.3

1-й вариант

С помощью обрезания строки ".".join(date[:4].split("-"))

![](png/z2.3.31.png)

2-й вариант

С помощью big.split('-') new_data = int(year)

![](png/z2.3.32.png)

3-й вариант

С помощью datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').strftime("%Y")

![](png/z2.3.33.png)

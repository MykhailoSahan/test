# Обчислення площі прямокутника
print("\nОбчислення площі прямокутника\n")
print("Введіть вихідні дані:\n")
print("Довжина (см.) -> ", end="")
l = float(input())
print("Ширина (см.) -> ", end="")
w = float(input())
s = l * w
print("-"*40)
print(f"Площа прямокутника: {s} кв. см\n")



# Обчислення площі paralelograma
print("Обчислення площі прямокутника")
print("Введіть вихідні дані:")
print("Висота (см.) -> ", end='')
h = float(input())
print("Основа (см.) -> ", end='')
a = float(input())
print("-"*35)
s = h * a
print(f"Площа прямокутника: {s} кв. см.\n")


#Обчислення вартості покупки
print("Обчислення вартості покупки")
print("Введіть вихідні дані:")
print("Ціна зошита (грн) -> ", end="")
#x = 2.75
x = float(input())
print("Ціна обкладинки (грн.) -> ", end="")
#y = 0.5
y = float(input())
print("К-сть комплектів (шт) -> ", end="")
#z = 7
z = float(input())
print("-"*35)
p = (x + y) * z
print(f"Вартість покупки: {p} грн.\n")



#Обчислення об'єму циліндра
print("Обчислення об'єму циліндра")
print("Введіть вихідні дані:")
print("Радіус основи (см) -> ", end="")
#r = 5
r = float(input())
print("Висота циліндра (см) -> ", end="")
#h2 = 10
h2 = float(input())
print("-"*35)
v = 3.14 * (r * r) * h2
print(f"Об'єм циліндра: {v}\n")




#Дохід
print("сума, грн -> ", end="")
suma = float(input())
print("Термін внеску, міс. -> ", end="")
month = float(input())
print("-"*35)
if suma < 5000:
    print("Відсоток річний: 10")
    prubytok = suma * 0.1;
else:
    print("Відсоток річний: 13")
    prubytok = suma * 0.13;
print(f"Прибуток: {prubytok} грн.")
if month == 12:
    End_Of = 10000 + prubytok;
print(f"Сума наприкінці строку вкладу: {End_Of} грн.\n")





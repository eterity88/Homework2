#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


number = float(input("Введите число: "))
while number != int(number):
    number *= 10
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(int(sum))
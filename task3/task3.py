#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! 

import random
 
list_1 = [5,10,4,9,11]
print("Первоначальный список : " + str(list_1))

for i in range(len(list_1)-1, 0, -1):

    j = random.randint(0, i + 1)

    list_1[i], list_1[j] = list_1[j], list_1[i]

print("Перемешанный список : " +  str(list_1))


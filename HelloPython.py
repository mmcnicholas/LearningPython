print("Hello World, this is Python!")
list1 = []
list1.append("Mr. Dursley")
list1.append("Mrs. Dursley")
list1.append("Dudley Dursley")
list1.append("Minerva McGonagall")
list1.append("Albus Dumbledore")
list1.append("Hagrid")
list1.append("Harry Potter")
list1.append("Tom")
list1.append("Quirrel")
print(list1)
print (sorted(list1))
# TODO: -ALL LOWERCASE NO PUNCTUATION TWO LINES BETWEEN EACH BOOK CHARACTER
# TODO: -ALL CHARACTERS BUT EVERY LETTER/NUMBER ON ITS OWN LINE
for item in list1:
    print (str.lower(item))

# import string
#
# for item in list1:
#     print (item.translate(string.punctuation))
#
# for item in list1:
#     print (str.lower(item.translate(string.punctuation)))

for item in list1:
    print (item)
    print("")
    print("")

for item in list1:
    for x in item:
        print (x)
    print("")

list2 = []
list3 = []
list2.append("Harry")
list2.append("Hermione")
list2.append("Ron")
list3.append("Potter")
list3.append("Granger")
list3.append("Weasley")

new_list =[]
for each in range(0,len(list2)):
         new_list.append(list2[each] + " " + list3[each])
print(new_list)

import numpy as np

arr2 = np.array(["Harry", "Hermione","Ron"])
arr3 = np.array(["Potter", "Granger", "Weasley"])

for i in range(0, 3):
    print(arr2[i] + " " + arr3[i])


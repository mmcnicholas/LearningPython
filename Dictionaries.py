from pprint import pprint

dict1 = {}
dict2 = {}

dict1["Harry"] = "Potter"
dict2["Hermione"] = "Granger"

dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)
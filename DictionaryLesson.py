from pprint import pprint

dict = {}

dict['key'] = 'value'
dict['harry'] = 'potter'


dict['harry'] = 'bush'

# print(dict)
#
# print(dict.keys())
#
# print(dict.values())

dict['florida state university'] = ['john doe', 'somebody else', 'vanessa']

dict.pop('harry')


print(dict)

for key, value in dict.items():
    print (key, value)


english_dict = {
    "dog": "dogs are a mands best friend",
    "cat": "Cats are aight"
}

german_dict = {
    "hund":"der hund es gruen",
    "kat":"holle hund"
}

dict_dict = {
    "en":english_dict,
    "ge":german_dict
}

pprint(dict_dict)

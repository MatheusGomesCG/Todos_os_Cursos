import requests
from Cep import BuscaEndereco

cep = "58434323"
objeto_cep = BuscaEndereco(cep)

# r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
# print(r.text)

a = objeto_cep.acessa_via_cep()
# print(a)
# print(type(a))
# print(dir(a))
print(type(a.text))
print(type(a.json()))
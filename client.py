import requests
from test import func_test

func_test()

base_url = "http://localhost:5007"

message = input("Entrez un msg : ")
data = {"message": message }

response = requests.post(base_url + "/message", json=data)

if response.status_code == 200:
    print("Réponse du serveur : ", response.json()["response"])
else:
    print("Erreur : ", response.json())


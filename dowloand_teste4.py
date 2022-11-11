import requests


url = "https://www.googleapis.com/drive/v3/files/1nKFJxRQ5Mk_kjGA0zjVYtSoEWBTErGD7"

payload={}
headers = {
  'Authorization': 

response = requests.get(url, headers=headers, data=payload)


open("dados_para_api", "wb").write(response.content)

import requests


url = "https://www.googleapis.com/drive/v3/files/1nKFJxRQ5Mk_kjGA0zjVYtSoEWBTErGD7"

payload={}
headers = {
  'Authorization': 'Bearer ya29.a0AeTM1ie7szIAN4kTcNBvXCPmxyOO4WTBbszxKJNfh-bgWJRazamW974UR08GljAka3UuWBxP1P9WjY7-YLoryZ6Xy-HpzthEr2GMRoqm3ETlHu5JfHlv6fRxXnM8OJ_rtCiiUzt2vZc7L30GLHEm41ixD91EDAaCgYKAa4SARESFQHWtWOmJK2uUdfQH2ND58E7cxEtew0165'
}

response = requests.get(url, headers=headers, data=payload)


open("dados_para_api", "wb").write(response.content)
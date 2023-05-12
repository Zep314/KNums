import requests

class Knum:
    def __init__(self):
        pass

    def get(self):
        print('hi')
        url = 'https://egrp365.org/list4.php?' \
              'street=Ломоносова' \
              '&street_type=ул' \
              '&house=35' \
              '&building=null' \
              '&mregion=Кировская' \
              '&area=null' \
              '&city=Киров' \
              '&settlement=null' \
              '&apartment=53' \
              '&link=page' \
              '&fiasid=null'

        headers = {'user-agent': 'my-app/0.0.1'}
        x = requests.get(url, headers=headers)
        print(url)
        print(x.status_code)
        print(x.json())
        return '123'
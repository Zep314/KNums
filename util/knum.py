import requests
import re

class Knum:
    def __init__(self):
        pass

    def get(self
            , street
            , street_type
            , house
            , building
            , settlement
            , type_town
            , apartment
            , fiasid
            ) -> object:

        if len(house) == 0: house = 'null'
        if len(building) == 0: building = 'null'
        if len(settlement) == 0: settlement = 'null'
        if len(apartment) == 0: apartment = 'null'
        if len(fiasid) == 0: fiasid = 'null'

        if type_town == 'г.':
            street += '(' + settlement +')'
            settlement = 'null'

        # url = 'https://egrp365.org/list4.php?' \
        #       'street=Ломоносова' \
        #       '&street_type=ул' \
        #       '&house=35' \
        #       '&building=null' \
        #       '&mregion=Кировская' \
        #       '&area=null' \
        #       '&city=Киров' \
        #       '&settlement=null' \
        #       '&apartment=53' \
        #       '&link=page' \
        #       '&fiasid=null'
        url = 'https://egrp365.org/list4.php?' \
              f'street={street}' \
              f'&street_type={street_type}' \
              f'&house={house}' \
              f'&building={building}' \
              '&mregion=Кировская' \
              '&area=null' \
              '&city=Киров' \
              f'&settlement={settlement}' \
              f'&apartment={apartment}' \
              '&link=page' \
              f'&fiasid={fiasid}'

        headers = {'user-agent': 'my-app/0.0.1'}
        x = requests.get(url, headers=headers)
        # print(url)
        # print(x.json())
        if (x.status_code == 200) and (x.json().get('error') == 0):
            data = x.json().get('data')
            if data.find('egrp=') > 0:
                data = data[data.find('egrp=') + 5:]
                data = data[:data.find('\'')]
                return ['0','', data]
            else:
                return ['1', 'Не могу распарсить', '']
        else:
            return ['1',re.sub(r'\<[^>]*\>', '', x.json().get('data')),'']

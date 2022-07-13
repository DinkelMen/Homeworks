import json
import requests
import xml.etree.ElementTree as ET
import yaml


'''1 задание'''
# response4 = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors').json()
# for dicts in response4:
#     for name in dicts:
#         if name == 'firstName' or name == 'lastName':
#             print(dicts[name])


# id = 5
# response5 = requests.get(url=f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{id}').json()
# print(response5['firstName'], response5['lastName'])


# body = {"id": 0, "title": "string", "description": "string", "pageCount": 0, "excerpt": "string", "publishDate": "2022-07-13T09:11:07.504Z"}
# response6 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books', json=body)
# print(response6)


# body2 = {"id": 0, "userName": "string", "password": "string"}
# response7 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users', json=body2)
# print(response7)


# id2 = 3
# body3 = {"id": 0, "title": "string", "description": "string", "pageCount": 0, "excerpt": "string", "publishDate": "2022-07-13T10:07:53.089Z"}
# response8 = requests.put(url=f'https://fakerestapi.azurewebsites.net/api/v1/Books/{id2}', json=body3)
# print(response8)


# id3 = 8
# response9 = requests.delete(url=f'https://fakerestapi.azurewebsites.net/api/v1/Users/{id3}')
# print(response9)


'''2 задание'''
# tree = ET.parse('library.xml')
# root = tree.getroot()
#
#
# def search(attribute):
#     for n in range(5):
#         for child in root[n]:
#             child_tag = child.tag
#             child_text = child.text
#             if attribute in child_text:
#                 print(root[n].tag, root[n].attrib)
#
#
# search('Zed')


'''3 задание'''

# with open('order.yaml', 'r') as f:
#     yaml_list = yaml.load(f, yaml.FullLoader)
#     print('Инвойс: ', yaml_list['invoice'])
#     print('Адрес: ', yaml_list['bill-to']['address'])
#     print('Описание посылки: ', yaml_list['product'])

# with open('order.json', 'w') as json_file:
#     json.dump(yaml_list, json_file, indent=4, sort_keys=True, default=str)

# with open('new_yaml_file.yaml', 'w') as yaml_file:
#     print('It is new Yaml file.')





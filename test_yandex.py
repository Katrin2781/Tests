import unittest
import requests
from Yandex_API import find_file, read_token, create_folder

FOLDERNAME = 'New folders'


class TestYandexAPI(unittest.TestCase):
    def test_find_file(self):
        result = find_file(FOLDERNAME)
        self.assertTrue(result == 200 or result == 404, f'Сервер ответил: {result}')

    def test_create_folder(self):
        res_def = create_folder(FOLDERNAME)
        token = read_token('Yandex')
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': token}
        params = {'path': '/'}
        result = requests.get(url, headers=headers, params=params).json()['_embedded']['items']
        for val in result:
            if FOLDERNAME == val['name']:
                res = True
                break
        else:
            res = False
        self.assertTrue(res == True or res_def == 201, f'Папка не найдена')
import requests
import configparser


def find_file(folder):
    params = {'path': folder}
    result = requests.get(url, headers=headers, params=params).status_code
    print(result)
    return result


def create_folder(name):
    if find_file(name) != 200:
        params = {'path': name}
        res = requests.put(url, headers=headers, params=params).status_code
        print(f'Папка {name} успешно создана!')
        return res
    else:
        print(f'Папка с именем {name} уже существует')


def read_token(access_obj):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    token = config[access_obj]['TOKEN']
    return token


token = read_token('Yandex')
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': token}

if __name__ == '__main__':
    print(create_folder('New folders'))



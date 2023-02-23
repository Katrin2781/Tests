def geo_logs(country):
    geo_logs_dict = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    geo_logs_country = []
    for dict_visit in geo_logs_dict:
        visit = list(dict_visit.values())
        if country in visit[0]:
            geo_logs_country.append(dict_visit)
    return geo_logs_country


def unique_values(dict_user):
    id_list = set()
    for value in dict_user.values():
        val_set = set(value)
        id_list = id_list | val_set
    return list(id_list)


def max_rating(dict_chanel):
    return max(dict_chanel, key = dict_chanel.get)


if __name__ == "__main__":
    # 1 задание
    rez = geo_logs('Россия')

    # 2 задание
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(unique_values(ids))

    # 3 задание
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    print(f'Канала с максимальным объемом - {max_rating(stats)}')
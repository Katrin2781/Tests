import pytest
from task1 import geo_logs, unique_values, max_rating


@pytest.mark.parametrize("country_in, country_out", [
    ('Россия', 'Россия'),
    ('Индия', 'Индия'),
    ('Португалия','Португалия')])
def test_get_dict(country_in, country_out):
    res = geo_logs(country_in)
    for item in res:
        assert list(item.values())[0][1] == country_out
        

def test_unique_values():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    res = unique_values(ids)
    assert res == [98, 35, 213, 54, 119, 15]

@pytest.mark.parametrize("dict_chanal, chanal", [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 155, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook'),
    ({'facebook': 155, 'yandex': 120, 'vk': 215, 'google': 99, 'email': 42, 'ok': 98}, 'vk')])
def test_max_rating(dict_chanal, chanal):
    res = max_rating(dict_chanal)
    assert res == chanal
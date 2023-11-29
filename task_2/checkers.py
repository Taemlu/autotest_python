import requests
import pytest
import yaml


with open('config.yaml') as f:
    conf = yaml.safe_load(f)
    url = conf["url"]
    login = conf["login"]
    password = conf["password"]
    url_get = conf["url_get"]
    ttl = conf["ttl"]


def test_get_token(get_token):
    response = requests.post(url=url,
                           data={"username": login, "password": password})
    #print(response.json())
    res_token = response.json()["token"]
    #print(res_token)
    assert response.status_code == 200
    assert res_token == get_token


def test_check_post(get_token, request_get):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(url_get, headers=headers, params={'owner': 'notMe'})
    posts = response.json()
    #print(f"check{posts}")
    assert response.status_code == 200
    assert posts == request_get


if __name__ == "__main__":
    pytest.main(['-vv'])
import requests
base_url="http://172.0.0.1"
from requests import  Session
# 登录接口
def test_add_customer():
    """测试添加客户"""
    ses = requests.Session()
    # 登录
    login_url = base_url + "/api/mgr/signin"
    login_data = {"username": "byhy", "password": "88888888"}
    ses.post(login_url, data=login_data)

    # 添加客户
    add_url = base_url + "/api/mgr/customers"
    add_data = {
        "action": "add_customer",
        "name": "pytest医院",
        "address": "上海"
    }
    add_res = ses.post(add_url, json=add_data)
    assert add_res.json()["ret"] == 0
    print('yes')


def test_modify_customer():
    """测试修改客户（先添加再修改）"""
    ses = requests.Session()
    # 登录
    login_url = base_url + "/api/mgr/signin"
    login_data = {"username": "byhy", "password": "888888"}
    ses.post(login_url, data=login_data)

    # 先添加一个客户
    add_url = base_url + "/api/mgr/customers"
    add_data = {
        "action": "add_customer",
        "name": "待修改医院",
        "address": "北京"
    }
    add_res = ses.post(add_url, json=add_data)
    customer_id = add_res.json()["id"]  # 假设返回里有 id

    # 修改这个客户
    modify_url = base_url + "/api/mgr/customers"
    modify_data = {
        "action": "modify_customer",
        "id": customer_id,
        "name": "已修改医院",
        "address": "上海"
    }
    modify_res = ses.put(modify_url, json=modify_data)  # 也可能是 post
    assert modify_res.json()["ret"] == 0


def test_delete_customer():
    """测试删除客户（先添加再删除）"""
    ses = requests.Session()
    # 登录
    login_url = base_url + "/api/mgr/signin"
    login_data = {"username": "byhy", "password": "888888"}
    ses.post(login_url, data=login_data)

    # 先添加一个客户
    add_url = base_url + "/api/mgr/customers"
    add_data = {
        "action": "add_customer",
        "name": "待删除医院",
        "address": "广州"
    }
    add_res = ses.post(add_url, json=add_data)
    customer_id = add_res.json()["id"]

    # 删除这个客户
    delete_url = base_url + "/api/mgr/customers"
    delete_data = {
        "action": "del_customer",
        "id": customer_id
    }
    delete_res = ses.delete(delete_url, json=delete_data)  # 也可能是 post
    assert delete_res.json()["ret"] == 0


test_add_customer()
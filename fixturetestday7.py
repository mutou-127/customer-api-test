
import requests


def test_list(login_session):  # 参数名必须和 fixture 名字一样
    # 这里可以直接用 login_session，它已经登录好了
    params = {"action": "list_customer", "pagesize": 1}
    res = login_session.get("http://127.0.0.1/api/mgr/customers", params=params)
    assert res.status_code == 200


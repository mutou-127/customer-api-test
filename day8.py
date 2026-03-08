import pytest
import requests

@pytest.fixture()
def login_session():
    ses=requests.Session()
    login_url='http://127.0.0.1/api/mgr/signin'
    login_data={"username": "byhy", "password": "88888888"}
    ses.post(url=login_url,data=login_data)
    return ses


def test_list(login_session):
    parmas={'action':'list_customer','pagesize':1,'pagenum':1}
    res=login_session.get('http://127.0.0.1/api/mgr/customers',params=parmas)
    assert res.status_code==200

@pytest.mark.parametrize('name,phone,address',[
    ('yuuan1','13822389483','beiing'),
    ('yuuanB','12982329382','shangai'),
    ('yuyunC','28392814283','sguanzhou')
])
def test_add(login_session,name,phone,address):
    data={
        'action': 'add_customer',
        'data':{'name': name,  # 从参数化传进来的名字
        'phonenumber': phone,  # 从参数化传进来的电话
        'address': address  }# 从参数化传进来的地址
    }
    res=login_session.post("http://127.0.0.1/api/mgr/customers", json=data)
    print(res.json())
    assert res.json()['ret']==0

def test_modify(login_session):
    add_data={
        'action':'add_customer',
        'data':{
            'name':'待修改医院',
            'phonenumber':'1380013022',
            'address':'北京'
        }
    }
    add_res=login_session.post("http://127.0.0.1/api/mgr/customers", json=add_data)
    assert add_res.json()['ret']==0
    csutomer_id=add_res.json()['id']

    modify_data={
        'action': 'modify_customer',
        'id':csutomer_id,
        'newdata': {
            'name': '已经修改医院',
            'phonenumber': '1380023000',
            'address': '北京2'
        }
    }
    modify_res=login_session.put("http://127.0.0.1/api/mgr/customers",json=modify_data)
    assert modify_res.json()['ret']==0

def test_delete(login_session):
    add_data={
        'action':'add_customer',
        'data':{
            'name':'待删除医院',
            'phonenumber':'1380013022',
            'address':'北京'
        }
    }
    add_res=login_session.post("http://127.0.0.1/api/mgr/customers", json=add_data)
    assert add_res.json()['ret']==0
    customer_id=add_res.json()['id']

    delete_data = {
        'action': 'del_customer',
        'id': customer_id
    }
    delete_res=login_session.delete("http://127.0.0.1/api/mgr/customers", json=delete_data)
    assert delete_res.json()['ret']==0





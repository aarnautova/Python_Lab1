import requests

url = 'http://127.0.0.1:5000'   # The root url of the flask app


def test_create():
    r = requests.post(
        url+'/flowers',
        json={"name": "1", "time": "12", "days": []})
    obj = r.json()
    assert obj.get("name") == "1"
    assert obj.get("time") == "12"
    assert obj.get("days") == []
    assert r.status_code == 201


def test_get_by_id():
    r = requests.post(
        url + '/flowers',
        json={"name": "1", "time": "12", "days": []})
    obj = r.json()
    period_id = str(obj.get("period_id"))
    res = requests.get(url + '/flowers/' + period_id)
    o = res.json()
    assert o.get("name") == "1"
    assert o.get("time") == "12"
    assert o.get("days") == []
    assert res.status_code == 200
    requests.delete(url + '/flowers/' + period_id)


def test_delete():
    r = requests.post(
        url + '/flowers',
        json={"name": "1", "time": "12", "days": []})
    obj = r.json()
    period_id = str(obj.get("period_id"))
    res = requests.delete(url + '/flowers/' + period_id)
    assert res.status_code == 200


def test_upd():
    r = requests.post(
        url + '/flowers',
        json={"name": "1", "time": "12", "days": []})
    obj = r.json()
    period_id = int(obj.get("period_id"))
    res = requests.put(
        url + '/flowers',
        json={"period_id": period_id, "time": "12:50", "days": ["Friday"]})
    # o = res.json()
    assert res.status_code == 200

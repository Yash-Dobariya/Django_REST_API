import requests
import json

URL = 'http://127.0.0.1:8000/student_api'

def get_data(id = None):
    data = {}

    if id is not None:
        data = {'id': id}

    headers = {'content-Type': 'application/json'}
    json_data =  json.dumps(data)
    r = requests.get(url= URL, headers= headers, data= json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
        'name': 'rohan',
        'roll':'120',
        'city':'Surat'
    }

    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)
     
# post_data()

def update_data():
    data = {
        'id':3,
        'name': 'Rohan',
        'city':'Ahmadabad',
        'roll': '104'
    }

    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)
     
# update_data()

def delete_data():
    data = {
        'id': 3
    }

    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, headers=headers, data= json_data)
    data = r.json()
    print(data)

# delete_data()
import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds161443.mlab.com:61443/phamvantu

#mongodb://<dbuser>:<dbpassword>@ds159208.mlab.com:59208/a-task
#v2:
#mongodb://<dbuser>:<dbpassword>@ds135519.mlab.com:35519/a-task-v2
host = "ds161443.mlab.com"
port = 61443
db_name = "phamvantu"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
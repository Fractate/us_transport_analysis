import json
def retrieve_default_state():
    f = open('./config.json')
    data = json.load(f)
    state = data['STATE']
    f.close()
    return state

def retrieve_default_geographic_level():
    f = open('./config.json')
    data = json.load(f)
    state = data['GEOGRAPHIC_LEVEL']
    f.close()
    return state

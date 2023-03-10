import argparse
import os
import hashlib
import hmac
import json
import requests
from xml.etree import ElementTree
from pick import pick
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', default='192.168.1.1')
parser.add_argument('--username', default='admin')
parser.add_argument('--password', default='admin')
parser.add_argument('--warning-level', default=1)
parser.add_argument('--disable-level', default=3)
args = parser.parse_args()

hostname = args.hostname
username = args.username
password = args.password
warning_lvl = args.warning_level
disable_lvl = args.disable_level

url = f'http://{hostname}/api/1.0/'


def auth_hash(token, username, password):
    fh_1 = hashlib.sha256(username.encode()).hexdigest()
    key_hash_1 = hmac.new(token.encode(), msg=fh_1.encode(), digestmod=hashlib.sha256).hexdigest()
    fh_2 = hashlib.sha256(password.encode()).hexdigest()
    key_hash_2 = hmac.new(token.encode(), msg=fh_2.encode(), digestmod=hashlib.sha256).hexdigest()
    return key_hash_1 + key_hash_2


def auth(url, username, password):
    authenticated = False

    r = requests.get(f'{url}?method=auth.getToken')
    data = utils.etree_to_dict(ElementTree.fromstring(r.content))

    token = data['rsp']['auth']['@token']
    key_hash = auth_hash(token, username, password)

    r = requests.get(f'{url}?method=auth.checkToken&token={token}&hash={key_hash}')
    data = utils.etree_to_dict(ElementTree.fromstring(r.content))

    if not data['rsp']['@stat'] == 'ok':
        print(f'[INFO][AUTH] {data}')
    else:
        authenticated = True
        print(f'[INFO][AUTH] OK')

    return token, authenticated


token, is_authenticated = auth(url, username, password)

with open('api.json', 'r') as f:
    api = json.load(f)


def api_cmd(api, token, w_lvl=warning_lvl, d_lvl=disable_lvl):
    options = list(api.keys())
    option, index = pick(options)
    api_1 = option

    api = api[api_1]
    options = list(api.keys())
    option, index = pick(options)
    api_2 = option

    api = api[api_2]
    api_call = api_1 + '.' + api_2
    api_method = api['requestMethods']
    api_access = api['access']
    api_args = api['args']
    api_warning = api['warning']

    if api_warning >= d_lvl:
        raise PermissionError

    if api_warning >= w_lvl:
        if not utils.query_yes_no(f'{api_call} may be unsafe, do you confirm ?'):
            raise UserWarning

    if api_access == 'private':
        api_call += f'&token={token}'

    for i in range(len(api_args)):
        api_call += f'&{api_args[i]}=' + input(f'> {api_args[i]} : ')

    req = f'{url}?method={api_call}'
    if api_method == 'GET':
        print('GET ', req)
        r = requests.get(req)
    elif api_method == 'POST':
        print('POST', req)
        r = requests.post(req)
    else:
        raise NotImplementedError

    # r.text without blank lines
    print(os.linesep.join([s for s in r.text.splitlines() if s]))


while True:
    input("Press Enter to continue...")
    try:
        api_cmd(api, token)
    except Exception as e:
        print("Exception:", type(e).__name__)

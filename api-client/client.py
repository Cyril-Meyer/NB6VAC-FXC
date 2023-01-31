import argparse
import hashlib
import hmac
import requests
from xml.etree import ElementTree
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', default='192.168.1.1')
parser.add_argument('--username', default='admin')
parser.add_argument('--password', default='admin')
args = parser.parse_args()

hostname = args.hostname
username = args.username
password = args.password
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

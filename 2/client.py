import json
import requests

API_ENDPOINT = 'http://10.4.21.156'
MAX_DEG = 11


def urljoin(root, path=''):
    if path:
        root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root


def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id': id, 'vector': vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


def get_errors(id, vector):
    for i in vector:
        assert 0 <= abs(i) <= 10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))


def get_overfit_vector(id):
    return json.loads(send_request(id, [0], 'getoverfit'))


def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector:
        assert 0 <= abs(i) <= 10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')


# Replace 'SECRET_KEY' with your team's secret key (Will be sent over email)
if __name__ == "__main__":
    # vec = [0.0, -5.498623626605807e-17, 1.0710572500094568e-05, 9.162639673800067e-08, -0.488224282309279, 1.503261394372703e-20,
    #        6.979320815739931e-20, 4.5871138220146244e-12, 2.100124387118824e-12, -4.6930862102660125e-12, -1.814498505183458e-11]
    # Error around 1.5e12
    # vec = [0.0, -7.036530793256614e-17, 8.190293699420056e-06, 9.169178213323054e-08, -0.5675880864964316, 1.2691328044590184e-20,
    #        6.212489781204206e-20, 4.25125587563371e-12, 2.333939393981563e-12, -4.265359988654308e-12, -1.3583568917940034e-11]
    # Error around 1.38e12
    # vec = [0.0, -5.431987843423241e-17, 1.3239767111253694e-05, 1.0718326376963613e-07, -0.6052635114299969, 1.5833859453747286e-20,
    #        8.312210574165536e-20, 4.385594023517787e-12, 2.3063103570781153e-12, -5.34037552365445e-12, -1.0256566832203762e-11]
    # Error around 1.35e12
    vec = [0.0, -5.105223582356095e-17, 1.1502848718805467e-05, 1.0453861891304721e-07, -0.6602970352859908, 1.826048426945547e-20,
           1.0271695115197742e-19, 3.6009629713447435e-12, 1.7683040901200354e-12, -5.158054865509138e-12, -4.982287992001061e-12]
    # Error around 1.31e12
    print(submit("w6zmexNbwRHCKVKxAjTMN7kU4SOsMsoXL5cEAZKoHfvi0F0tvY", vec))

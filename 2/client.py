import json
import requests
import numpy as np

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
    # vec = [0.0, -8.371130232983974e-17, 9.025142615136325e-06, 8.486515372411621e-08, -0.09989371994094633, 1.639489074835743e-20,
    #        5.374296710645325e-20, 4.312415114171999e-12, 3.0500027922125163e-12, -5.645393439138087e-12, -5.626917493926551e-12]
    vec = [0.0, -5.739853894592857e-17, 1.0486894453670895e-05, 9.006398275736896e-08, -0.2843416280532337, 1.4035322589824344e-20,
           5.196081453071491e-20, 4.57376192955343e-12, 2.4923643994885166e-12, -4.463965589081825e-12, -1.3098617239505182e-11]
    print(submit("w6zmexNbwRHCKVKxAjTMN7kU4SOsMsoXL5cEAZKoHfvi0F0tvY", vec))

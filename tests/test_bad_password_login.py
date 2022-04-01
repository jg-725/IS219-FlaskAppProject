"""This tests bad password in Login page """

from flaskr import flaskr

def login(client, password):
    return client.post('/login', data=dict(
        password=password
    ), follow_redirects=True)

def test_login_password(client):
    response = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'] + 'x')
    # Check the bad password.
    assert b'Invalid password: Does not meet the criteria' in response.data
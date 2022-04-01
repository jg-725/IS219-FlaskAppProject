"""This test's if password does not meet criteria in registration page """

from flaskr import flaskr

def login(client, password):
    return client.post('/register', data=dict(
        password=password
    ), follow_redirects=True)

def test_password_criteria(client):
    response = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'] + 'xx')
    # Check password with bad criteria.
    assert b'Password DOES NOT MEET criteria!' in response.data

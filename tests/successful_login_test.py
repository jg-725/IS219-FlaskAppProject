"""This test's if user successfully logged in """

from flaskr import flaskr

def login(client, email, password):
    return client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)

def test_successful_login(client):
    response = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'])
    # Check the bad email/username.
    assert b'Congrats, You were logged in!' in response.data
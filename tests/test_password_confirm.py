"""This test's password confirmation in the registration page """

from flaskr import flaskr

def login(client, password, confirm):
    return client.post('/register', data=dict(
        password=password,
        confirm=confirm
    ), follow_redirects=True)

def test_successful_login(client):
    response = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'])
    # Check the bad email/username.
    assert b'Both Passwords are the same!' in response.data
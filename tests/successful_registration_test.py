"""This test's if user successfully registered """

from flaskr import flaskr

def login(client, email, password, confirm):
    return client.post('/register', data=dict(
        email=email,
        password=password,
        confirm=confirm
    ), follow_redirects=True)

def test_successful_registration(client):
    response = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'], flaskr.app.config['PASSWORD'])
    # Check the bad email/username.
    assert b'Congrats, You were Registered Properly!' in response.data
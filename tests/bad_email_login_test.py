"""This test's bad username/email in the Login page """

from flaskr import flaskr

def login(client, email):
    return client.post('/login', data=dict(
        email=email
    ), follow_redirects=True)

def test_login_email(client):
    response = login(client, flaskr.app.config['USERNAME'] + 'x', flaskr.app.config['PASSWORD'])
    # Check the bad email/username.
    assert b'Invalid email' in response.data
"""This test's bad username/email in the Register page """

def test_bad_email_register(bad_email_register):
    assert bad_email_register.email == 'example123@email.com'
    assert bad_email_register.password == 'Password'
    assert bad_email_register.confirm == 'Password'
    response = bad_email_register.get("/register")
    assert response.status_code == 302
    assert b'Invalid email ' in response.data
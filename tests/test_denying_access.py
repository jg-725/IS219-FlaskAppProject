"""This tests denying access to users NOT logged in """

def test_deny_access(bad_user):
    assert bad_user.email == 'example@email.com'
    assert bad_user.password == 'Password1'
    response = bad_user.get("/")
    assert response.status_code == 302
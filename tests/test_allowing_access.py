"""This tests allowing access to logged in users """

def test_access(new_user):
    assert new_user.email == 'example@email.com'
    assert new_user.password == 'Password'
    response = new_user.get("/dashboard")
    assert response.status_code == 302
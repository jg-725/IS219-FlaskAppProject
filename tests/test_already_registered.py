"""This test's if user is already registered """

def test_duplicate_register(new_user):
    assert new_user.email == 'example@email.com'
    assert new_user.password == 'Password'
    response = new_user.get("/login")
    assert response.status_code == 300
    assert b'User is already registered' in response.data
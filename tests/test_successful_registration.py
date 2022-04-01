"""This test's if user successfully registered """

def test_successful_register(successful_registration):
    assert successful_registration.email == 'example@email.com'
    assert successful_registration.password == 'Password'
    assert successful_registration.confirm == 'Password'
    response = successful_registration.get("/dashboard")
    assert response.status_code == 302
    assert b'Congrats, registration success' in response.data
"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app
from app.auth import login_form
from app.auth import register_form

@pytest.fixture()
def application():
    """This makes the app"""
    application = create_app()
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()


@pytest.fixture()
def new_user():
    user = login_form('example@email.com', 'Password')
    return user


@pytest.fixture()
def bad_user():
    user = login_form('example@email.com', 'Password1')
    return user


@pytest.fixture()
def successful_registration():
    user = register_form('example@email.com', 'Password', 'Password')
    return user


@pytest.fixture()
def bad_email_register():
    user = register_form('example123@email.com', 'Password', 'Password')
    return user
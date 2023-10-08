import allure
from jsonschema.validators import validate
from test.conftest import reqres_api
from utils.helper import load_schema


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check status code')
def test_users_status_code():
    response = reqres_api(
        method='get',
        url='/users'
    )
    assert response.status_code == 200


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check per_page param')
def test_users_per_page():
    per_page = 3

    response = reqres_api(
        method='get',
        url='/users',
        params={'per_page': per_page}
    )
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check user schema')
def test_user_schema():
    schema = load_schema('get_users_schema.json')
    response = reqres_api(
        method='get',
        url='/users'
    )
    validate(instance=response.json(), schema=schema)


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check "User not found" status code')
def test_users_not_found_status_code():
    response = reqres_api(
        method='get',
        url='/users/23'
    )
    assert response.status_code == 404


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check create user')
def test_create_user():
    response = reqres_api(
        method='post',
        url='/users',
        data={'name': 'TestUser',
              'job': 'Worker'}
    )
    assert response.status_code == 201
    assert response.json()['name'] == 'TestUser'
    assert response.json()['job'] == 'Worker'


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check create user schema')
def test_schema_create_user():
    schema = load_schema('create_user_schema.json')

    response = reqres_api(
        method='post',
        url='/users',
        data={'name': 'TestUser',
              'job': 'Worker'}
    )
    validate(instance=response.json(), schema=schema)


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check delete user')
def test_delete_user():
    response = reqres_api(
        method='delete',
        url='/users/693'
    )
    assert response.status_code == 204


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check registration')
def test_user_registration():
    response = reqres_api(
        method='post',
        url='/register',
        data={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )
    assert response.status_code == 200


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check failed registration')
def test_user_registration_failed():
    response = reqres_api(
        method='post',
        url='/register',
        data={
            "email": "eve.holt@reqres.in",
            }
    )
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


@allure.label('owner', 'Roman Sh')
@allure.tag('API')
@allure.feature('Reqres.in test')
@allure.title('Check update user')
def test_user_update():
    response = reqres_api(
        method='patch',
        url='/users/2',
        data={
            'name': 'Test',
            'job': 'worker'
        }
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'Test'
    assert response.json()['job'] == 'worker'

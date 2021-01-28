import pytest
from jsonschema import validate

from main import app


@pytest.fixture(scope="session")
def client():
    """Prepare flask test client for all unit tests."""
    app.testing = True
    return app.test_client()


def test_endpoints_status_code(client):
    """Test all endpoints and wrong url status codes."""
    assert client.get('/').status_code == 200
    assert client.get('/boardgames').status_code == 200
    assert client.get('/boardgames/2').status_code == 200
    assert client.get('/categories').status_code == 200
    assert client.get('/invalid').status_code == 404


def test_endpoints_cors(client):
    """Test all endpoints and wrong url CORS header."""
    assert client.get('/').headers.get('Access-Control-Allow-Origin') == '*'
    assert client.get('/boardgames').headers.get('Access-Control-Allow-Origin') == '*'
    assert client.get('/boardgames/2').headers.get('Access-Control-Allow-Origin') == '*'
    assert client.get('/categories').headers.get('Access-Control-Allow-Origin') == '*'
    assert client.get('/invalid').headers.get('Access-Control-Allow-Origin') == '*'


def test_endpoints_json_schema(client):
    """Test all endpoints JSON schema."""
    schema_list = {'type': 'array'}
    schema_dict = {'type': 'object'}
    schema_list_dicts = {'type': 'array', 'items': {'type': 'object'}}

    assert validate(client.get('/boardgames').get_json(), schema_list_dicts) is None
    assert validate(client.get('/boardgames/2').get_json(), schema_dict) is None
    assert validate(client.get('/categories').get_json(), schema_list) is None


def test_boardgames_padding(client):
    """Test padding on /boardgames endpoint."""
    total_records = int(client.get('/boardgames').headers['X-Total-Count'])
    expected_pages = (total_records - 1) // 20 + 1

    assert len(client.get('/boardgames').get_json()) == 20
    assert len(client.get('/boardgames?limit=10').get_json()) == 10
    assert client.get('/boardgames').get_json() == client.get('/boardgames?page=1').get_json()
    assert client.get('/boardgames?limit=10&page=1').get_json() + client.get(
        '/boardgames?limit=10&page=2').get_json() == client.get('/boardgames?limit=20&page=1').get_json()
    assert client.get(f'/boardgames?page={expected_pages+1}').status_code == 404
    assert client.get('/boardgames?page=0').status_code == 404
    assert client.get('/boardgames?page=-1').status_code == 404
    assert client.get('/boardgames?limit=0').get_json() == []
    assert client.get('/boardgames?limit=-1').status_code == 404


def test_categories(client):
    """Test data returned in categories endpoint."""
    total_records = int(client.get('/boardgames').headers['X-Total-Count'])
    expected_categories = set()
    for record in client.get(f'/boardgames?limit={total_records}').get_json():
        expected_categories.update(set(record['categories']))

    assert expected_categories == set(client.get('/categories').get_json())


def test_boardgames_categories(client):
    """Test boardgames endpoint filter by categories (picked one rare, one common, not joined)."""
    categories = client.get('/categories').get_json()

    assert client.get('/boardgames?category').get_json() == []
    assert client.get('/boardgames?category=invalid').get_json() == []
    for record in client.get(f'/boardgames?category={categories[1]}').get_json():
        assert categories[1] in record['categories']
    for record in client.get(f'/boardgames?category={categories[5]}').get_json():
        assert categories[5] in record['categories']
    for record in client.get(f'/boardgames?category={categories[1]}&category={categories[5]}').get_json():
        assert (categories[1] in record['categories']) or (categories[5] in record['categories'])


def test_boardgames_sort(client):
    total = int(client.get('/boardgames').headers['X-Total-Count'])
    ids = [record['id'] for record in client.get('/boardgames').get_json()]
    total_ids = [record['id'] for record in client.get(f'/boardgames?limit={total}').get_json()]
    names = [record['name'] for record in client.get('/boardgames?sort_by=name').get_json()]
    total_names = [record['name'] for record in client.get(f'/boardgames?limit={total}&sort_by=name').get_json()]

    assert ids == sorted(ids)
    assert total_ids == sorted(total_ids)
    assert names == sorted(names, key=lambda char: char.replace(':', ''))
    assert total_names == sorted(total_names, key=lambda char: char.replace(':', ''))

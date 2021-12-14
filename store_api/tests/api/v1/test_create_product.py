import json
import pytest

def test_create_new_product(monkeypatch, test_app):
    ''' Test creating new product with a valid payload '''
    test_request_payload = {
        'name': "product",
        'description': "description",
        'price': 10.50
    }
    test_response_payload = {
        'message': "Product created successfully",
        'product_id': 1,
    }

    async def mock_post(payload):
        payload = 1
        return payload

    monkeypatch.setattr('app.api.v1.services.products.post.post', mock_post)

    response = test_app.post('/v1/products', data=json.dumps(test_request_payload))

    assert response.status_code == 201

    assert response.json() == test_response_payload

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{}, 422],
        [{'name': "n", 'description': "de", 'price': -10}, 422],
        [{'name': "n", 'description': "de", 'price': 'a'}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "de", 'price': -10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "de", 'price': 'a'}, 422],
        [{'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [{'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
    ],
)

def test_create_new_product_with_invalid_payload(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid payload '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{'name': "n", 'description': "description", 'price': 10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "description", 'price': 10}, 422],
        [{'description': "description", 'price': 10}, 422],
    ],
)

def test_create_new_product_with_invalid_name(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid name '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{'name': "valid name", 'description': "de", 'price': 10}, 422],
        [{'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [{'name': "valid name", 'price': 10}, 422],
    ],
)

def test_create_new_product_with_invalid_description(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid description '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{'name': "valid name", 'description': "description", 'price': 'a'}, 422],
        [{'name': "valid name", 'description': "description", 'price': -1}, 422],
        [{'name': "valid name", 'description': "description"}, 422],
    ],
)

def test_create_new_product_with_invalid_price(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid price '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{'name': "n", 'description': "d", 'price': 10}, 422],
        [{'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "d", 'price': 10}, 422],
        [{'price': 10}, 422],
    ],
)

def test_create_new_product_with_invalid_name_and_description(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid name and description '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
   'payload, status_code',
    [
        [{'name': "n", 'description': "description", 'price': -10}, 422],
        [{'name': "n", 'description': "description", 'price': 'a'}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "description", 'price': -10}, 422],
        [{'name': "A name bigger than 30 characters", 'description': "description", 'price': 'a'}, 422],
        [{'description': "description"}, 422],
    ],
)

def test_create_new_product_with_invalid_name_and_price(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid name and price '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{'name': "valid name", 'description': "de", 'price': -10}, 422],
        [{'name': "valid name", 'description': "de", 'price': 'a'}, 422],
        [{'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [{'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
        [{'name': "valid name"}, 422],
    ],
)

def test_create_new_product_with_invalid_description_and_price(test_app, monkeypatch, payload, status_code): #pylint: disable=unused-argument
    ''' Test creating new product with invalid description and price '''

    response = test_app.post('/v1/products', data=json.dumps(payload))

    assert response.status_code == status_code

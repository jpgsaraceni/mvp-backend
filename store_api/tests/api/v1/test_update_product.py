#pylint: disable=line-too-long
import json
import pytest

def test_update_product_by_id(test_app, monkeypatch):
    ''' Test the update of a valid product by its id '''
    test_request_payload = {
        'name': "Updated product",
        'description': "Updated description",
        'price': 10.55,
        'image': None
    }
    test_response_payload = {
        'message': "Product updated successfully",
        'product_id': 1
    }

    async def mock_get(product_id):
        return {
            'id': product_id,
            'name': "Product",
            'description': "Description",
            'price': 10.50,
            'image': None
        }

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    async def mock_put(product_id, payload): #pylint: disable=unused-argument
        return product_id

    monkeypatch.setattr('app.api.v1.services.products.put.put', mock_put)

    response = test_app.put('/v1/products/1', data=json.dumps(test_request_payload))

    assert response.status_code == 202
    assert response.json() == test_response_payload

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [-1, {'name': "Updated product", 'description': "Updated description", 'price': 10.55, 'image': None}, 400],
        [999, {'name': "Updated product", 'description': "Updated description", 'price': 10.55, 'image': None}, 404],
        ['a', {'name': "Updated product", 'description': "Updated description", 'price': 10.55, 'image': None}, 422],
    ]
)

def test_update_product_with_invalid_id(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test update product with invalid id '''

    async def mock_get(product_id): #pylint: disable=unused-argument
        return None

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {}, 422],
        [1, {'name': "n", 'description': "de", 'price': -10}, 422],
        [1, {'name': "n", 'description': "de", 'price': 'a'}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "de", 'price': -10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "de", 'price': 'a'}, 422],
        [1, {'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [1, {'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_payload(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid payload '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {'name': "n", 'description': "description", 'price': 10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "description", 'price': 10}, 422],
        [1, {'description': "description", 'price': 10}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_name(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid name '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {'name': "valid name", 'description': "de", 'price': 10}, 422],
        [1, {'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [1, {'name': "valid name", 'price': 10}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_description(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid description '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {'name': "valid name", 'description': "description", 'price': 'a'}, 422],
        [1, {'name': "valid name", 'description': "description", 'price': -1}, 422],
        [1, {'name': "valid name", 'description': "description"}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_price(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid price '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {'name': "n", 'description': "d", 'price': 10}, 422],
        [1, {'name': "n", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "d", 'price': 10}, 422],
        [1, {'price': 10}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_name_and_description(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid name and description '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
   'product_id, payload, status_code',
    [
        [1, {'name': "n", 'description': "description", 'price': -10}, 422],
        [1, {'name': "n", 'description': "description", 'price': 'a'}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "description", 'price': -10}, 422],
        [1, {'name': "A name bigger than 30 characters", 'description': "description", 'price': 'a'}, 422],
        [1, {'description': "description"}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_name_and_price(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid name and price '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

@pytest.mark.parametrize(
    'product_id, payload, status_code',
    [
        [1, {'name': "valid name", 'description': "de", 'price': -10}, 422],
        [1, {'name': "valid name", 'description': "de", 'price': 'a'}, 422],
        [1, {'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': -10}, 422],
        [1, {'name': "valid name", 'description': "This is an invalid product description because it has more than 140 characters, it is bigger than a tweet, so it is ridiculous, horrible, such a crime", 'price': 'a'}, 422],
        [1, {'name': "valid name"}, 422],
    ],
)

def test_update_product_with_valid_id_but_invalid_description_and_price(test_app, monkeypatch, product_id, payload, status_code): #pylint: disable=unused-argument
    ''' Test updating new product with invalid description and price '''

    response = test_app.put(f'/v1/products/{product_id}', data=json.dumps(payload))

    assert response.status_code == status_code

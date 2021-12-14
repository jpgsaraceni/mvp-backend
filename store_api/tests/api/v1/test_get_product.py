import pytest

def test_get_product_by_id(test_app, monkeypatch):
    ''' Test fetching a valid product by its id '''
    test_response_payload = {
        'id': 1,
        'name': "Product",
        'description': "Description",
        'price': 10.50,
        'image': None
    }

    async def mock_get(_):
        return test_response_payload

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    response = test_app.get('/v1/products/1')

    assert response.status_code == 200
    assert response.json() == test_response_payload

@pytest.mark.parametrize(
    'product_id, status_code',
    [
        [-3, 400],
        [999, 404],
        ['a', 422]
    ]
)

def test_get_product_by_invalid_id(test_app, monkeypatch, product_id, status_code):
    ''' Test fetching a product by invalid id '''

    async def mock_get(_):
        return None

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    response = test_app.get(f'/v1/products/{product_id}')

    assert response.status_code == status_code

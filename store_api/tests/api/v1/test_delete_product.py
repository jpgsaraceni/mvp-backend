import pytest

def test_delete_product_by_id(test_app, monkeypatch):
    ''' Test the correct deletion of a product by its id '''
    test_response_payload = {
        'message': "Product deleted successfully",
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

    async def mock_delete(product_id):
        return product_id

    monkeypatch.setattr('app.api.v1.services.products.delete.delete', mock_delete)

    response = test_app.delete('/v1/products/1')

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

def test_delete_product_by_invalid_id(test_app, monkeypatch, product_id, status_code):
    ''' Test the deletion of a product by invalid id '''

    async def mock_get(_):
        return None

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    response = test_app.delete(f'/v1/products/{product_id}')

    assert response.status_code == status_code

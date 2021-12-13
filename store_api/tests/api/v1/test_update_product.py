import json

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

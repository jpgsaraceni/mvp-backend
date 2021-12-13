import json

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

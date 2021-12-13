def test_get_product_by_id(test_app, monkeypatch):
    ''' Test fetching a valid product by its id '''
    test_response_payload = {
        'id': 1,
        'name': "Product",
        'description': "Description",
        'price': 10.50,
        'image': None
    }

    async def mock_get(product_id): #pylint: disable=unused-argument
        return test_response_payload

    monkeypatch.setattr('app.api.v1.services.products.get.get', mock_get)

    response = test_app.get('/v1/products/1')

    assert response.status_code == 200
    assert response.json() == test_response_payload

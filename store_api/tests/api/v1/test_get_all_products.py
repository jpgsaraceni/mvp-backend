def test_get_all_products(test_app, monkeypatch):
    ''' Test listing all products '''
    test_response_payload = [
        {
        'id': 1,
        'name': "Product1",
        'description': "Description1",
        'price': 10.50,
        'image': None
        },
        {
        'id': 2,
        'name': "Product2",
        'description': "Description2",
        'price': 20.50,
        'image': None
        },
    ]

    async def mock_get_all():
        return test_response_payload

    monkeypatch.setattr('app.api.v1.services.products.get_all.get_all', mock_get_all)

    response = test_app.get('/v1/products')

    assert response.status_code == 200
    assert response.json() == test_response_payload

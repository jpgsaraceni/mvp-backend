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

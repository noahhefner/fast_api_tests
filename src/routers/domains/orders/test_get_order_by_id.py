def test_get_order_by_id(client):
    response = client.get("/api/orders/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")

    assert response.status_code == 200
    assert response.json()["address"] == "123 Main St, Springfield, USA"

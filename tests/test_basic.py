def test_health_check():
    from api.app import create_app
    app = create_app()
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

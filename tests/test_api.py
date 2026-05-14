from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


# 1. Health check responde corretamente
def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# 2. Endpoint clima funciona (caso sucesso)
def test_clima_sucesso():
    response = client.get("/api/v1/clima/Fortaleza")
    assert response.status_code == 200


# 3. Endpoint clima - erro 404
def test_clima_404():
    response = client.get("/api/v1/clima/CidadeInexistenteXYZ")
    assert response.status_code == 404


# 4. Endpoint clima - erro 400
def test_clima_400():
    response = client.get("/api/v1/clima/12345")
    assert response.status_code == 400


# 5. Endpoint cidades por estado funciona
def test_cidades_sucesso():
    response = client.get("/api/v1/cidades/CE?limite=5")
    assert response.status_code == 200


# 6. Endpoint cidades - erro 404
def test_cidades_404():
    response = client.get("/api/v1/cidades/ZZ")
    assert response.status_code == 404


# 7. Endpoint cidades - erro 400
def test_cidades_400():
    response = client.get("/api/v1/cidades/123")
    assert response.status_code == 400
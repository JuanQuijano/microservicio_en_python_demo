import pytest
from suma import create_app

# Configura el entorno para pruebas
@pytest.fixture(scope="session")
def app():
    # Asegúrate de que se use la configuración de pruebas
    # os.environ["PYMS_CONFIGMAP_FILE"] = "config-tests.yml"
    app = create_app
    return app

# Crea un cliente de prueba para la aplicación
@pytest.fixture(scope="module")
def client(app):
    return app.test_client()

# Obtiene la URL base del servicio
@pytest.fixture(scope="module")
def base_url(app):
    return app.config

# Prueba la ruta de salud del microservicio
def test_healthcheck(client, base_url):
    response = client.get(f"{base_url}healthcheck")
    assert response.status_code == 200
    assert b"Healthy" in response.data

# Prueba la suma de dos números
def test_sumar(client, base_url):
    data = {"cantidad1": 10, "cantidad2": 5}
    response = client.post(f"{base_url}sumar", json=data)
    assert response.status_code == 200
    assert response.json["resultado"] == 15

# Agrega más pruebas según tus necesidades
# ...

if __name__ == "__main__":
    pytest.main()

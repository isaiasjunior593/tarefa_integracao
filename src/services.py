# src/services.py

import httpx

tempo_limite = 10.0


def buscar_clima(cidade: str):
    try:
        geo = httpx.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": cidade,
                "count": 1,
                "language": "pt",
                "format": "json"
            },
            timeout=tempo_limite
        )

        geo.raise_for_status()

        resultados = geo.json().get("results")

        if not resultados:
            return None

        item = resultados[0]

        latitude = item["latitude"]
        longitude = item["longitude"]

        clima = httpx.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "daily": "temperature_2m_max,temperature_2m_min",
                "current_weather": "true",
                "timezone": "auto"
            },
            timeout=tempo_limite
        )

        clima.raise_for_status()

        dados_clima = clima.json()

        return {
            "cidade": item["name"],
            "estado": item.get("admin1", ""),
            "temperatura_min": dados_clima["daily"]["temperature_2m_min"][0],
            "temperatura_max": dados_clima["daily"]["temperature_2m_max"][0],
            "temperatura_atual": dados_clima["current_weather"]["temperature"]
        }

    except:
        return None


def listar_cidades(uf: str, limite: int):
    try:
        resposta = httpx.get(
            f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios",
            timeout=tempo_limite
        )

        if resposta.status_code != 200:
            return None

        lista = resposta.json()

        cidades = []

        for cidade in lista:
            cidades.append(cidade["nome"])

        return cidades[:limite]

    except:
        return None
# API Trabalho N703

API REST desenvolvida em Python com FastAPI para a disciplina **Técnicas de Integração de Sistemas**.

---

## Integrantes

Consultar arquivo `INTEGRANTES.md`.

---

## Tecnologias Utilizadas

* Python 3
* FastAPI
* Uvicorn
* HTTPX
* Pytest

---

## APIs Externas Utilizadas

* IBGE API (cidades e estados)
* Open-Meteo API (dados climáticos)

---

## Como Executar o Projeto

### 1. Instalar dependências

```bash id="bnv7oe"
pip install fastapi uvicorn httpx pytest
```

### 2. Executar servidor

```bash id="zot8b2"
py -m uvicorn src.main:app --reload
```

### 3. Acessar documentação interativa


```txt id="x1u4dm"
http://localhost:8000/docs
```

---

## Como Executar os Testes

### Testes automatizados com Pytest

```bash
py -m pytest
```

### Testes no Postman

Executar as requisições da collection:

```txt
docs/postman_collection.json
```

---


## Endpoints Disponíveis

### Health Check

```http id="mn2x4g"
GET /api/v1/health
```

Retorna o status da API.

---

### Buscar clima por cidade

```http id="yo1jv4"
GET /api/v1/clima/{cidade}
```

Exemplo:

```http id="6p2yqz"
GET /api/v1/clima/Fortaleza
```

---

### Listar cidades por estado

```http id="azr4ne"
GET /api/v1/cidades/{uf}?limite=5
```

Exemplo:

```http id="fdw6gk"
GET /api/v1/cidades/CE?limite=5
```

---

## Estrutura do Projeto

```txt id="ybn4rq"
/
├── README.md
├── INTEGRANTES.md
├── src/
├── tests/
└── docs/
    └── postman_collection.json
```

---

## Tratamento de Erros

* **400 Bad Request** → parâmetros inválidos
* **404 Not Found** → recurso não encontrado

---

## Observações

* Projeto acadêmico.
* API desenvolvida com foco em integração de sistemas.
* Dados retornados dependem da disponibilidade das APIs externas.


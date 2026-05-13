from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, UTC
from src.services import buscar_clima, listar_cidades

router = APIRouter()

UFS_VALIDAS = [
    "AC","AL","AP","AM","BA","CE","DF","ES","GO","MA",
    "MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN",
    "RS","RO","RR","SC","SP","SE","TO"
]


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "versao": "1.0.0",
        "timestamp": datetime.now(UTC).isoformat()
    }


@router.get("/clima/{cidade}")
def clima(cidade: str):

    if not cidade.replace(" ", "").isalpha():
        raise HTTPException(
            status_code=400,
            detail="Nome da cidade inválido"
        )

    dados = buscar_clima(cidade)

    if not dados:
        raise HTTPException(
            status_code=404,
            detail="Cidade não encontrada"
        )

    return dados


@router.get("/cidades/{uf}")
def cidades(
    uf: str,
    limite: int = Query(10, ge=1, le=100)
):

    uf = uf.upper()

    # erro 400 = formato errado
    if len(uf) != 2 or not uf.isalpha():
        raise HTTPException(
            status_code=400,
            detail="UF deve conter 2 letras"
        )

    # erro 404 = UF inexistente
    if uf not in UFS_VALIDAS:
        raise HTTPException(
            status_code=404,
            detail="UF inválida"
        )

    dados = listar_cidades(uf, limite)

    return {
        "uf": uf,
        "quantidade": len(dados),
        "cidades": dados
    }
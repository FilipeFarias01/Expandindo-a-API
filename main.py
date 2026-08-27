from fastapi import FastAPI

app = FastAPI()


# Banco de dados fictício
usuarios_db = [
    {
        "id": 1,
        "nome": "João",
        "cargo": "Desenvolvedor",
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Maria",
        "cargo": "Designer",
        "ativo": True
    },
    {
        "id": 3,
        "nome": "Carlos",
        "cargo": "Desenvolvedor",
        "ativo": False
    },
    {
        "id": 4,
        "nome": "Ana",
        "cargo": "Gerente",
        "ativo": True
    },
    {
        "id": 5,
        "nome": "Pedro",
        "cargo": "Designer",
        "ativo": False
    }
]


# 1. Retorna apenas usuários ativos
@app.get("/usuarios/ativos")
def listar_usuarios_ativos():
    usuarios_ativos = []

    for usuario in usuarios_db:
        if usuario["ativo"] == True:
            usuarios_ativos.append(usuario)

    return usuarios_ativos


# 2. Retorna apenas usuários inativos
@app.get("/usuarios/inativos")
def listar_usuarios_inativos():
    usuarios_inativos = []

    for usuario in usuarios_db:
        if usuario["ativo"] == False:
            usuarios_inativos.append(usuario)

    return usuarios_inativos


# 3. Retorna usuários filtrando pelo cargo
@app.get("/usuarios/cargo/{cargo}")
def listar_usuarios_por_cargo(cargo: str):
    usuarios_cargo = []

    for usuario in usuarios_db:
        if usuario["cargo"].lower() == cargo.lower():
            usuarios_cargo.append(usuario)

    return usuarios_cargo


# 4. Retorna informações gerais
@app.get("/info")
def obter_informacoes_gerais():
    total_usuarios = len(usuarios_db)

    total_ativos = 0
    total_inativos = 0

    for usuario in usuarios_db:
        if usuario["ativo"] == True:
            total_ativos += 1
        else:
            total_inativos += 1

    return {
        "total_usuarios": total_usuarios,
        "usuarios_ativos": total_ativos,
        "usuarios_inativos": total_inativos
    }

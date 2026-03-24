from fastapi import FastAPI
from clase import Pokemon
from storage import guardar, cargar
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # solucion a problema usar datos de api
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



DB_FILE = "data.dat"
pokemons = cargar(DB_FILE)


#Crear Pokémon
@app.post("/pokemon")
def crear_pokemon(nombre: str, numero: int, tipo: int, pc: int, nivel: int):
    nuevo = Pokemon(nombre, numero, tipo, pc, nivel)
    pokemons.append(nuevo)
    guardar(pokemons, DB_FILE)
    return {"mensaje": "Pokemon creado"}


#listar
@app.get("/pokemon")
def listar():
    return [p.to_dict() for p in pokemons]


#Buscar por número
@app.get("/pokemon/{numero}")
def buscar(numero: int):
    for p in pokemons:
        if p.numero == numero:
            return p.to_dict()
    return {"error": "No encontrado"}



@app.get("/tipo/{tipo}")
def por_tipo(tipo: int):
    res = []
    for p in pokemons:
        if p.tipo == tipo:
            res.append(p.to_dict())
    return res


#Eliminar por número
@app.delete("/pokemon/{numero}")
def eliminar(numero: int):
    global pokemons
    nueva = []
    eliminado = False

    for p in pokemons:
        if p.numero != numero:
            nueva.append(p)
        else:
            eliminado = True

    pokemons = nueva
    guardar(pokemons, DB_FILE)

    if eliminado:
        return {"mensaje": "Eliminado"}
    else:
        return {"error": "No encontrado"}

@app.get("/stats")
def estadisticas():
    m = [[0] * 6 for _ in range(18)]

    # cargar matriz
    for p in pokemons:
        f = p.tipo - 1
        c = p.nivel - 1
        if 0 <= f < 18 and 0 <= c < 6:
            m[f][c] += 1

    #totales por tipo (filas)
    totales_tipo = []
    for f in range(18):
        suma = 0
        for c in range(6):
            suma += m[f][c]
        totales_tipo.append(suma)

    #totales por nivel (columnas)
    totales_nivel = []
    for c in range(6):
        suma = 0
        for f in range(18):
            suma += m[f][c]
        totales_nivel.append(suma)

    max_val = 0
    max_f = max_c = 0

    for f in range(18):
        for c in range(6):
            if m[f][c] > max_val:
                max_val = m[f][c]
                max_f = f
                max_c = c

    return {
        "matriz": m,
        "totales_por_tipo": totales_tipo,
        "totales_por_nivel": totales_nivel,
        "maximo": {
            "tipo": max_f + 1,
            "nivel": max_c + 1,
            "cantidad": max_val
        }
    }

@app.get("/stats")
def estadisticas():
    filas = 18
    cols = 6
    m = [[0] * cols for _ in range(filas)]

    for p in pokemons:
        if 1 <= p.tipo <= filas and 1 <= p.nivel <= cols:
            f = p.tipo - 1
            c = p.nivel - 1
            m[f][c] += 1

    totales_tipo = [0] * filas
    for f in range(filas):
        suma = 0
        for c in range(cols):
            suma += m[f][c]
        totales_tipo[f] = suma

    totales_nivel = [0] * cols
    for c in range(cols):
        suma = 0
        for f in range(filas):
            suma += m[f][c]
        totales_nivel[c] = suma

    max_val = 0
    max_f = -1
    max_c = -1

    for f in range(filas):
        for c in range(cols):
            if m[f][c] > max_val:
                max_val = m[f][c]
                max_f = f
                max_c = c

    return {
        "matriz": m,
        "totales_por_tipo": totales_tipo,
        "totales_por_nivel": totales_nivel,
        "maximo": {
            "tipo": max_f + 1 if max_f != -1 else 0,
            "nivel": max_c + 1 if max_c != -1 else 0,
            "cantidad": max_val
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
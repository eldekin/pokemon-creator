#Pokemon Manager API + Frontend

Aplicación full stack desarrollada en Python y JavaScript que permite gestionar una colección de Pokémon mediante una API REST y un frontend web simple.

---

#Funcionalidades

- ✅ Crear Pokémon
- ✅ Listar Pokémon
- ✅ Eliminar Pokémon
- ✅ Estadísticas con matrices (tipo vs nivel)
- ✅ Persistencia de datos con archivos binarios (pickle)
- ✅ Frontend conectado a la API mediante fetch

---

#Tecnologías utilizadas

- **Backend:** Python + FastAPI
- **Frontend:** HTML + CSS + JavaScript (fetch)
- **Persistencia:** Pickle (archivos binarios)
- **Servidor:** Uvicorn

---

#Ejemplo de estadísticas

La aplicación genera una matriz de conteo:

- Filas → Tipo de Pokémon
- Columnas → Nivel

Incluye:
- Totales por tipo
- Totales por nivel
- Detección del máximo

---

# Cómo ejecutar el proyecto por cuenta propia

 1. Clonar repositorio

```bash
git clone https://github.com/tu-usuario/pokemon-api.git
cd pokemon-api

 2. Instalar dependencias 

pip install fastapi uvicorn

 3. Ejecutar servidor

uvicorn main:app --reload

4. Abrir Frontend

abrir archivo index.html
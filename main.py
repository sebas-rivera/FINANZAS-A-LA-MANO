from fastapi import FastAPI,Body
from app.v1.router.user_router import router as user_router
from app.v1.router.ingresos_router import router as Ingresos_router
from app.v1.router.fijos_router import router as Fijos_router
from app.v1.router.variables_router import router as Variables_router
from app.v1.router.retiros_router import router as Retiros_router

app = FastAPI(
    title = 'FINANZAS A LA MANO',
    description = 'Siempre a la mano'
)
app.include_router(user_router)
app.include_router(Ingresos_router)
app.include_router(Fijos_router)
app.include_router(Variables_router)
app.include_router(Retiros_router)

@app.get('/')
def home():
    return {"Ir a /docs para ver la api"}
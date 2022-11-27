from fastapi import FastAPI
from app.v1.router.user_router import router as user_router
from fastapi import Body
from app.v1.router.Ingresos_router import router as Ingresos_router


app = FastAPI()
app.include_router(user_router)
app.include_router(Ingresos_router)

@app.get('/')
def home():
    return {"Ir a /docs para ver la api"}

#uvicorn main:app --reload
from fastapi import FastAPI, Depends
from db.db import create_db_and_tables

# Need to import all the models to make sure the sql tables are created
from models.gem_models import *
from endpoints.user_endpoints import user_router
from auth.auth import AuthHandler

app = FastAPI()
auth_handler = AuthHandler()


@app.get(path="/")
def hello(user=Depends(auth_handler.auth_wrapper)):
    return "Hello World"

app.include_router(router=user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        port=8000,
        reload=True
    )
    create_db_and_tables()
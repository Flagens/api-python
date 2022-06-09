from fastapi import FastAPI
from rentapp.user import router as user_router
from rentapp.serviceApp import router as service_router
from rentapp.auth import router as auth_router

app = FastAPI(title="RentApp",
              version="1.0.0")

app.include_router(user_router.router)
app.include_router(service_router.router)
#app.include_router(auth_router.router)

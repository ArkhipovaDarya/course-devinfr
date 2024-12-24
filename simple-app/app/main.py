from fastapi import FastAPI
from app.database import engine, Base
from app.routers import router


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

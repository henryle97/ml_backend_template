import uvicorn 
from app.configs import settings

def serve():
    uvicorn.run(
        "main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )

if __name__ == "__main__":
    serve()
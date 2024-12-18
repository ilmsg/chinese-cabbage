from fastapi import FastAPI

def make_app() -> FastAPI:
    app: FastAPI = FastAPI()
    
    app.add
    
    return app


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        app=make_app(),
        port=7040,
        reload=True,
        loop="uvloop"
    )
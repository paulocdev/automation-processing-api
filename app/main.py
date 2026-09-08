from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/health")
def health_check():
    return 
    {
    "message": "API funcionando",
    "service": "automation-processing-api",
    "status": "ok"
    }

@app.get("/info")
def info():
    return
    {
        "project": "automation-processing-api",
        "version": "0.1.0",
        "status": "ok"
    }
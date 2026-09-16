from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"message": "NIVI backend is running"}
  

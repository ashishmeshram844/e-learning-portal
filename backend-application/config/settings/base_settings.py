from fastapi import FastAPI

app = FastAPI(docs_url=None, 
              redoc_url='/docs',
              title="E Learning Portal",
              version="0.0.1",
              description="E learning portal Api's for interacting with database",
          )
# from typing import Union

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from routers import task, done

# app = FastAPI()

# origins = [
#     "*"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app = FastAPI()
# app.include_router(task.router)
# app.include_router(done.router)

from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World"}
from fastapi import FastAPI

from app.exceptions.no_data_exception import NoDataException, no_data_exception_handler
from app.routers import country, indicator

app = FastAPI()

app.add_exception_handler(NoDataException, no_data_exception_handler)

app.include_router(country.router)
app.include_router(indicator.router)


@app.get("/")
async def status():
    return {"status": "Ok"}

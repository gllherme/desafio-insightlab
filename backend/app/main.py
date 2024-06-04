from fastapi import FastAPI

from app.routers import country, indicator

from app.exceptions.no_data_exception import NoDataException, no_data_exception_handler
from app.exceptions.bad_filter_value_exception import BadFilterValueException, bad_filter_exception_handler

app = FastAPI()

app.add_exception_handler(NoDataException, no_data_exception_handler)
app.add_exception_handler(BadFilterValueException,
                          bad_filter_exception_handler)

app.include_router(country.router)
app.include_router(indicator.router)


@app.get("/")
async def status():
    return {"status": "Ok"}

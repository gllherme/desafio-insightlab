from pydantic import BaseModel


class CountryCode(BaseModel):
    code: str
    name: str

# class CountryCodeResponse(BaseModel):

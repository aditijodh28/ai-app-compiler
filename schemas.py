from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]

class AppSpec(BaseModel):
    ui: dict
    api: dict
    database: dict
    auth: dict
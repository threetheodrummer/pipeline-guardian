from pydantic import BaseModel

class Finding(BaseModel):
    id: str
    severity: str
    description: str | None = None

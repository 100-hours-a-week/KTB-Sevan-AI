from pydantic import BaseModel, ConfigDict

class SummaryResponse(BaseModel):
    id: int
    content: str

    model_config = ConfigDict(from_attributes=True)
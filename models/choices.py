from pydantic import BaseModel


class ChoiceBase(BaseModel):
    text: str


class Choice(ChoiceBase):
    id: int
    poll_id: int

    class Config:
        orm_mode = True


class ChoiceVotes(ChoiceBase):
    id: int
    count: int


class ChoiceCreate(ChoiceBase):
    pass


class ChoiceUpdate(ChoiceBase):
    pass

from enum import Enum

from pydantic import BaseModel

from models.choices import ChoiceCreate, Choice


class PollKind(str, Enum):
    SINGLE_CHOICE = 'single choice'
    MULTIPLE_CHOICES = 'multiple choices'


class PollBase(BaseModel):
    choices: list[Choice]
    title: str
    description: str

    class Config:
        orm_mode = True


class Poll(PollBase):
    id: int
    user_id: int


# в дальнейшем могут появиться поля, которые не будут нужны при отображении
# но будут нужны при создании
class PollCreate(PollBase):
    choices: list[ChoiceCreate]


class PollUpdate(PollBase):
    choices: list[ChoiceCreate]


from pydantic import BaseModel

from models.choices import ChoiceVotes


class VoteBase(BaseModel):
    pass


class Vote(VoteBase):
    id: int
    voter_id: int
    choice_id: int

    class Config:
        orm_mode = True


class VoteCreate(VoteBase):
    pass


class VoteUpdate(VoteBase):
    pass


class VotesCount(BaseModel):
    poll_id: int
    choice_made: int | None = None
    choices: list[ChoiceVotes]

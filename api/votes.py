from typing import List

from fastapi import Depends
from fastapi import APIRouter
from fastapi import Response
from fastapi import status

from models.auth import User
from models.polls import Poll
from models.votes import VotesCount
from services.auth import get_current_user
from services.votes import VotesService

router = APIRouter(
    prefix='/polls',
)


@router.get("/get_votes_by_poll/{poll_id}")  # , response_model=VotesCount
def get_votes_by_poll(
    poll_id: int,
    user: User = Depends(get_current_user),
    service: VotesService = Depends(),
):
    return service.get_votes_count_by_poll(poll_id=poll_id, user_id=user.id)


@router.post("/vote")  # , response_model=VotesCount
def vote(
    choice_id: int,
    user: User = Depends(get_current_user),
    service: VotesService = Depends(),
):
    return service.vote(user_id=user.id, choice_id=choice_id)

from typing import List

from fastapi import Depends
from fastapi import APIRouter
from fastapi import Response
from fastapi import status

from models.auth import User
from models.polls import Poll, PollKind, PollCreate, PollUpdate
from services.auth import get_current_user
from services.polls import PollsService

router = APIRouter(
    prefix='/polls',
)


@router.get("/", response_model=List[Poll])
def get_polls(
    poll_kind: PollKind | None = None,
    user: User = Depends(get_current_user),
    service: PollsService = Depends(),
):
    return service.get_list(user_id=user.id, poll_kind=poll_kind)


@router.post('/', response_model=Poll)
def create_poll(
    poll_data: PollCreate,
    user: User = Depends(get_current_user),
    service: PollsService = Depends(),
):
    return service.create(user_id=user.id, poll_data=poll_data)


@router.get('/{poll_id}', response_model=Poll)
def get_poll(
    poll_id: int,
    user: User = Depends(get_current_user),
    service: PollsService = Depends()
):
    return service.get(user_id=user.id, poll_id=poll_id)


@router.delete('/{poll_id}', response_model=Poll)
def delete_poll(
    poll_id: int,
    user: User = Depends(get_current_user),
    service: PollsService = Depends()
):
    service.delete(user_id=user.id, poll_id=poll_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

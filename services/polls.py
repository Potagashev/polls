from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

import models
import tables
from database import get_session
from models.polls import PollKind, PollCreate, PollUpdate, Poll
from services.choices import ChoicesService


class PollsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, poll_id: int) -> tables.Poll:
        poll = (
            self.session
            .query(tables.Poll)
            .filter_by(
                id=poll_id,
                user_id=user_id
            )
            .options(
                joinedload('choices')
            )
            .first()
        )
        if not poll:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return poll

    def get_list(self, user_id: int, poll_kind: PollKind | None = None) -> List[tables.Poll]:
        query = (
            self.session
            .query(tables.Poll)
            .filter_by(user_id=user_id)
            .options(
                joinedload('choices')
            )
        )
        if poll_kind:
            query = query.filter_by(poll_kind=poll_kind)
        polls = query.all()
        return polls

    def get(self, user_id: int, poll_id: int) -> tables.Poll:
        return self._get(user_id=user_id, poll_id=poll_id)

    def create(self, user_id: int, poll_data: PollCreate) -> tables.Poll:
        poll = tables.Poll(
            user_id=user_id,
            title=poll_data.title,
            description=poll_data.description,
        )
        self.session.add(poll)
        self.session.commit()
        choicesService = ChoicesService(session=self.session)
        choicesService.create_many(poll_id=poll.id, choices_data=poll_data.choices)
        return poll

    def delete(self, user_id: int, poll_id: int):
        poll = self._get(user_id=user_id, poll_id=poll_id)
        self.session.delete(poll)
        self.session.commit()

    # def update(self, user_id: int, poll_id: int, poll_data: PollUpdate) -> tables.Poll:
    #     poll = self._get(user_id=user_id, poll_id=poll_id)
    #
    #     choicesService = ChoicesService(session=self.session)
    #     choicesService.delete_choices_in_poll(poll_id=poll_id)
    #     choicesService.create_many(poll_id=poll.id, choices_data=poll_data.choices)
    #
    #     for field, value in poll_data:
    #         setattr(poll, field, value)
    #     self.session.commit()
    #     return poll

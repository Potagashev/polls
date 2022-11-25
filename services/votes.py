from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql.functions import coalesce

import models.votes
import tables
from database import get_session
from models.votes import VotesCount
from responses import NOT_VOTED_RESPONSE_403, ALREADY_VOTED_403


class VotesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_votes_count_by_poll(self, user_id: int, poll_id: int) -> dict:
        choice_made = (
            self.session
            .query(tables.Vote.choice_id)
            .filter_by(voter_id=user_id)
            .filter(tables.Vote.choice.has(poll_id=poll_id))
            # .scalar_subquery()
            .all()
        )

        poll_owner_id = (
            self.session
            .query(tables.Poll.user_id)
            .filter_by(id=poll_id)
        )[0]
        if user_id != poll_owner_id:
            if choice_made is None:
                raise NOT_VOTED_RESPONSE_403

        choices = (
            self.session
            .query(
                tables.Choice.id,
                tables.Choice.text,
                func.count(tables.Vote.id).label('count')
            )
            .join(
                tables.Vote,
                tables.Choice.id == tables.Vote.choice_id,
                isouter=True
            )
            .filter(tables.Choice.poll_id == poll_id)
            .group_by(
                tables.Choice.id,
                tables.Choice.text
            ).all()
        )
        result = {
            'poll_id': poll_id,
            'choices': choices
        }
        if choice_made:
            result['choice_made'] = choice_made[0]
        else:
            result['choice_made'] = None
        return result

    def vote(self, user_id: int, choice_id: int) -> dict:
        existing_vote = (
            self.session
            .query(tables.Vote)
            .filter_by(voter_id=user_id, choice_id=choice_id)
            .all()
        )
        poll_id = (
            self.session
            .query(tables.Choice.poll_id)
            .filter_by(id=choice_id)
            .first()
        )[0]
        print(poll_id)
        if existing_vote:
            raise ALREADY_VOTED_403
        vote = tables.Vote(
            voter_id=user_id,
            choice_id=choice_id
        )
        self.session.add(vote)
        self.session.commit()
        return self.get_votes_count_by_poll(poll_id=poll_id, user_id=user_id)

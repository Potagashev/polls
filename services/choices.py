from fastapi import Depends
from sqlalchemy.orm import Session

import tables
from database import get_session
from models.choices import ChoiceCreate


class ChoicesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_choices_by_poll_id(self, poll_id: int) -> list[tables.Choice]:
        choices = (
            self.session
            .query(tables.Choice)
            .filter_by(
                poll_id=poll_id,
            ).all()
        )
        return choices

    def create_many(self, poll_id: int, choices_data: list[ChoiceCreate]):
        for choice in choices_data:
            new_choice = tables.Choice(text=choice.text, poll_id=poll_id)
            self.session.add(new_choice)
        self.session.commit()

    def delete_choices_in_poll(self, poll_id: int):
        choices = self._get_choices_by_poll_id(poll_id=poll_id)
        self.session.delete(choices)
        self.session.commit()

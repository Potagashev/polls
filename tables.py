from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, unique=True)
    username = Column(Text, unique=True)
    password_hash = Column(Text)


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, unique=True, index=True)
    description = Column(String)

    # user = relationship("User", back_populates="polls")
    choices = relationship("Choice", back_populates="poll")


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    poll_id = Column(Integer, ForeignKey("polls.id"))

    poll = relationship("Poll", back_populates="choices")
    votes = relationship("Vote", back_populates="choice")


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey('users.id'))
    choice_id = Column(Integer, ForeignKey("choices.id"))

    choice = relationship("Choice", back_populates="votes")

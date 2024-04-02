from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

Base = declarative_base()

router = Router()


class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id_chat = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    usernames = Column(String)


class Winner(Base):
    __tablename__ = 'winners'
    id_Winner = Column(Integer, primary_key=True)
    winner_id = Column(String)
    chat_id = Column(Integer)
    timestamp = Column(DateTime)


engine = create_engine('sqlite:///chat.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@router.message(Command("pidorlist"))
async def get_winners_table(message: Message):
    chat_id = message.chat.id

    participants = session.query(ChatMessage).filter_by(chat_id=chat_id).all()
    if participants:
        participant_list = [participant.usernames for participant in participants]
        answer_phrase = f'Держи список кандидатов в пидорасы: {", ".join(participant_list)}'
    else:
        answer_phrase = "Ой, а тут никого..."

    await message.answer(answer_phrase)

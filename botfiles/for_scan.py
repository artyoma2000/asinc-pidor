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


@router.message(Command("pidorscan"))
async def get_winners_table(message: Message):
    chat_id = message.chat.id
    username = message.from_user.username
    answer_phrase = ''
    try:
        chat_message = session.query(ChatMessage).filter_by(chat_id=chat_id).all()
        chat_message_list = [participant.usernames for participant in chat_message]
        print(chat_message_list)
        if not username in chat_message_list:
            chat_message = ChatMessage(chat_id=chat_id, usernames=username)
            session.add(chat_message)
            answer_phrase = "Записываю тебя в список пидорасов! Пока карандашиком..."
        else:
            answer_phrase = 'Эй, ты уже в игре!'

    except AttributeError:
        chat_message = ChatMessage(chat_id=chat_id, usernames=username)
        session.add(chat_message)
        answer_phrase = "Записываю тебя в список пидорасов! Пока карандашиком..."

    session.commit()
    await message.answer(answer_phrase)
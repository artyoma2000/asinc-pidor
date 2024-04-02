from sqlalchemy import create_engine, Column, String, Integer, DateTime
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


# Подключение к базе данных или создание новой, если не существует
def create_database():
    engine = create_engine('sqlite:///chat.db')
    Base.metadata.create_all(engine)


# Получение таблицы победителей в виде строки
# Получение таблицы победителей в виде строки
def get_winners_table(message):
    engine = create_engine('sqlite:///chat.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    chat_id = message.chat.id
    winners = session.query(Winner).filter_by(chat_id=chat_id).all()
    winners_count = {}
    for winner in winners:
        if winner.winner_id in winners_count:
            winners_count[winner.winner_id] += 1
        else:
            winners_count[winner.winner_id] = 1

    table = "Уровень пидорства:\n"
    for winner_id, count in winners_count.items():
        table += f"{winner_id} - {count}\n"

    return table


@router.message(Command("pidorstatic"))  # [2]
async def cmd_start(message: Message):
    create_database()
    await message.answer(
        get_winners_table(message)
    )

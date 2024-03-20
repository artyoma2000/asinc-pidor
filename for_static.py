from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

Base = declarative_base()


# Определение модели таблицы победителей
class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    winner_id = Column(String)
    timestamp = Column(DateTime)


# Подключение к базе данных или создание новой, если не существует
def create_database():
    engine = create_engine('sqlite:///bot.db')
    Base.metadata.create_all(engine)


# Получение таблицы победителей в виде строки
# Получение таблицы победителей в виде строки
def get_winners_table():
    engine = create_engine('sqlite:///bot.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    winners = session.query(Winner).all()
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
        get_winners_table()
    )

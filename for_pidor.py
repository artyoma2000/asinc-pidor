from random import choice
from datetime import datetime
import time
import random
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot_prases import random_element
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

text = [['Это просто ВОСХИТИТЕЛЬНО! Я ещё никогда не видел более гейского гея!',
         'Я понял, теперь я определитель пидора...',
         'Итак... кто же сегодня САМЫЙ ГЕЙСКИЙ ГЕЙ?',
         'Опять Влад буквы забыл?',
         'Осторожно! У Влада чесотка ануса',
         'Сейчас мы выясним кто тут пидарюга',
         ' Анус взломан. Нанесён урон. Запущен зонд',
         'дайте поспать, мне в падлу писать то, что и так понятно',
         'Я КАМЕНЩИК Я НЕ СПАЛ ТРИ ДНЯ',
         'Ну чё разбудили то... готовьте жопы'],
        ['Ведётся поиск в базе дебилов',
         'Крыша едет не спеша, тихо шифером шурша',
         'Выезжаю на место взлома жопы',
         'Ну и где он?',
         'Машины выехали зря. Владу хватит всего одной',
         'У него вообще есть конкуренты?',
         'Интересно было бы выбирать хотя бы из двух..',
         'я устал выбирать его. не зовите меня! или добавьте пидорасов',
         'Апчхи! правду говорю',
         'Хм... Я ебанулся или он правда уникален?',
         'После такой работы должны морфий выдавать...',
         'А мог бы сейчас чем-то интересным заняться!'],
        ['Знакомое лицо!',
         'Высокий приоритет по пидору',
         'Пидор слева!!!',
         'Я буду шмалять!',
         'Как же я ору с этого дебила',
         'Снова ты?',
         'Стоит на асфальте он в лыжи обутый, он видимо даун и ебанутый',
         'Ох ё. Это не ты на голой вечеринке был туалетом?',
         ' ЕЩЁ РАЗ ПОВТОРЯЮ ПРОДИКТУЙТЕ ВАШЕ ИМЯ ПО БУКВАМ',
         'Так, что тут у нас разрешённого?',
         'z ghjcnj rfr ,s nfr',
         'Zа chto mne dali eto zadanie',
         'Что же с нами стало...',
         'Я в опасности, системы повреждены смертельной дозой кринжа!']]

USER_IDS = ["@Vlados_9606", "@holyskot4", '@sokol347', '@rusak_set', '@xeniaos', '@dzennicherotzakroi', 'Роман, без '
                                                                                                        'ника в телеге']

router = Router()

Base = declarative_base()

engine = create_engine('sqlite:///bot.db', echo=True)
Session = sessionmaker(bind=engine)


class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    winner_id = Column(String)
    timestamp = Column(DateTime)


def create_database():
    Base.metadata.create_all(engine)


def choose_winner():
    with Session() as session:
        last_timestamp_str = session.query(Winner.timestamp).order_by(Winner.timestamp.desc()).first()
        if last_timestamp_str:
            last_timestamp = last_timestamp_str[0]
            today = datetime.now()

            if last_timestamp.date() <= today.date():
                return 'Сегодня уже выбран пидор дня. Скорые выехали зря.'

        if choice([True, False]):
            winner_id = USER_IDS[0]  # Select first element with 50% probability
        else:
            winner_id = choice(USER_IDS[1:])  # Select randomly from rest of the list
        timestamp = datetime.now()

        new_winner = Winner(winner_id=winner_id, timestamp=timestamp)
        session.add(new_winner)
        session.commit()

        return f'{random_element()} {winner_id}'


@router.message(Command("pidor"))
async def cmd_start(message: Message):
    create_database()
    k = choose_winner()
    if k != 'Сегодня уже выбран пидор дня. Скорые выехали зря.':
        for i in text:
            await message.answer(
                f'{random.choice(i)}'
            )
            time.sleep(1)
    await message.answer(
        k
    )

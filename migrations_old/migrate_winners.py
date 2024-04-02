import sqlite3
from datetime import datetime

# Подключаемся к базе данных
conn = sqlite3.connect('../chat.db')
cursor = conn.cursor()

# Очищаем таблицу winners
cursor.execute("DELETE FROM winners")

# Данные для вставки
winners = [
    ('dzennicherotzakroi', 1731170238),
    ('Vlados_9606', 1731170238),
    ('Vlados_9606', 1731170238),
    ('Vlados_9606', 1731170238),
    ('Vlados_9606', 1731170238),
    ('xeniaos', 1731170238),
    ('rusak_set', 1731170238),
    ('Роман, без ника в телеге', 1731170238),
    ('sokol347', 1731170238)
]

# Добавляем данные в таблицу winners
for id_Winner, winner_id in enumerate(winners, start=1):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO winners (id_Winner, winner_id, chat_id, timestamp) VALUES (?, ?, ?, ?)",
                   (id_Winner, winner_id[0], winner_id[1], timestamp))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
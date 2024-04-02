import sqlite3

# Список никнеймов участников чата
usernames = ["Vlados_9606", "holyskot4", 'sokol347', 'rusak_set', 'xeniaos', 'dzennicherotzakroi', 'Роман, без ника в телеге']

# Подключение к базе данных
conn = sqlite3.connect('../chat.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM chat_messages")

# Создание таблицы chat_messages, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS chat_messages 
                (id_chat INTEGER PRIMARY KEY,
                 chat_id INTEGER,git 
                 usernames TEXT)''')

# Заполнение таблицы chat_messages
chat_id = 1731170238
for id_chat, username in enumerate(usernames, start=1):
    cursor.execute("INSERT INTO chat_messages (id_chat, chat_id, usernames) VALUES (?, ?, ?)", (id_chat, chat_id, username))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
import asyncio
from aiogram import Bot, Dispatcher
from botfiles import for_static, for_pidor, for_list, for_scan
from config_reader import config


# Запуск бота
async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(for_pidor.router, for_static.router, for_list.router, for_scan.router)
    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
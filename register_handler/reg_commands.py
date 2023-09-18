from aiogram import Dispatcher

from handler.commands import cmd_start, cmd_setting, cmd_status


async def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(cmd_setting, commands=["setting"], state="*")
    dp.register_message_handler(cmd_status, commands=["status"], state="*")
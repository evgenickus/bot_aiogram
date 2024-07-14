import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import asyncio
import os
from dotenv import load_dotenv
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

load_dotenv()
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
  url = "https://images.assetsdelivery.com/compings_v2/katrink03/katrink031707/katrink03170700046.jpg"
  await message.answer(
    text=f"Hello, {markdown.hide_link(url=url)} {markdown.hbold(message.from_user.full_name)}!",
    parse_mode=ParseMode.HTML,
    )

@dp.message(Command("help"))
async def handle_help(message: types.Message):
  # text = "I'am an echo bot.\nSend me any message!"
  # entity_bold = types.MessageEntity(
  #   type="bold",
  #   offset=len("I'am an echo bot.\nSend me "),
  #   length=3,
  # )
  # entities = [entity_bold]
  # await message.answer(text=text, entities=entities)

  text = "I'am an echo bot\\.\nSend me *any* message\\!"
  text = markdown.text(
    markdown.markdown_decoration.quote("I'am an echo bot."),
    markdown.text(
      "Send me",
      markdown.markdown_decoration.bold(
        markdown.text(
          markdown.underline("literally"),
          "any",
        ),
      ),
    markdown.markdown_decoration.quote("message!"),
    ),
    sep="\n"
  )
  await message.answer(
    text=text,
    # parse_mode=ParseMode.MARKDOWN_V2,
  )
@dp.message(Command("code"))
async def handle_command_code(message: types.Message):
  text = markdown.text(
    "Here's Python code",
    "",
    markdown.markdown_decoration.pre_language(
      markdown.text(
        "print('Hello World!')",
        "\n",
        "def foo():\n    return 'bar'",
        sep="\n",
      ),
      language="python",
    ),
    "And here's some JS",
    "",
    markdown.markdown_decoration.pre_language(
      markdown.text(
        "console.log('Hello World!')",
        "\n",
        "function foo {\n  return 'bar'\n}",
        sep="\n",
      ),
      language="javascript",
    ),
    sep="\n",
  )
  await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):

  await message.answer(
    text="Wait a second..",
    parse_mode=None,

  )
  # if message.text:
  #   await message.answer(
  #     text=message.text,
  #     entities=message.entities,
  #   )


  try:
    await message.send_copy(chat_id=message.chat.id)
  except:
    await message.reply(text="Something new ")

async def main():
  logging.basicConfig(level=logging.INFO)
  bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
    )
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())




  
  # await message.bot.send_message(
  #   chat_id=message.chat.id,
  #   text="Start processing..",
  # )

  # await message.bot.send_message(
  #   chat_id=message.chat.id,
  #   text="Detected a message..",
  #   reply_to_message_id=message.message_id,
  # )

  # await message.answer(text="Start processing..")
  # await message.reply(text="Wait a second..")

    # if message.text:
  #   await message.reply(text=message.text)
  # elif message.sticker:
  #   await message.reply_sticker(sticker=message.sticker.file_id)
  # else:
  #   await message.reply(text="Something new ")

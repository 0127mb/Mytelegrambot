import telebot
import time

TOKEN = "SIZNING_BOT_TOKENINGIZ"
OWNER_ID = " 7956973654"  # O'z Telegram ID'ingizni shu yerga yozing

bot = telebot.TeleBot(8144123680:AAGjYrIk1rJqrKt128i8n1AFvol1ARIJA6U)

# Bot ishga tushganda egasiga xabar yuborish
def send_start_message():
    try:
        bot.send_message(OWNER_ID, "Salom (Odilova Xurshida siz uchun yaratildim) 😊")
    except Exception as e:
        print(f"Xabar yuborishda xatolik: {e}")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom! Men Telegram botman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Botni ishga tushirish
if __name__ == "__main__":
    send_start_message(Salom bu men telegram botman Odilova Xurshida siz uchun yaratildim)  # Bot ishga tushganda xabar yuboradi

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            time.sleep(1)


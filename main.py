from telegram.ext import Updater, CommandHandler, MessageHandler  # Подключение нужных функций из модуля telegram
from telegram.ext import Filters as F
from telegram.constants import PARSEMODE_MARKDOWN
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from model import load_data
# from sklearn.neural_network import MLPClassifier

# x_train, x_test, y_train, y_test = load_data(test_size=0.25)
# model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
# model.fit(x_train,y_train)
#
# print('model created!')

# def infer(path):
#     X = extract_feature(my_voice, True, True, True)

def start (update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='''
Hello! 
This bot can recognize 4 human emotions by your speech. 
Wanna try?
*Just send me something by voicemail!*
    ''', parse_mode=PARSEMODE_MARKDOWN)



def audio(update, context):
    name = update.message.from_user.first_name
    user_id = update.message.chat_id
    print(name, user_id)

    audio = context.bot.getFile(update.message.voice.file_id)
    audio.download('audios/audio_{}'.format(user_id))
    msg = '''
Seems like... Emotion of your voice message was {}
    '''.format('sad')
    context.bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=[])


TOKEN = '1766937694:AAGqj_K3euBfVoY2my3vDirn3YflycU0brg'

updater = Updater(token=TOKEN, workers=4)  # Создаём переменную типа (Updater) с аргументом token, который равен переменной TOKEN

dispatcher = updater.dispatcher  # Создаём диспетчер, который будет хранить все Handler'ы.

dispatcher.add_handler(CommandHandler('start', start, run_async=True))

dispatcher.add_handler(MessageHandler(F.voice, audio, run_async=True))


updater.start_polling()
updater.idle()

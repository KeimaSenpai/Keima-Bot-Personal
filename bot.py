import os
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import time

def start(update, context):
    name = update.effective_user['first_name']

    update.message.reply_text(
        text=(
            f'Hola {name}, este es el bot de @Keima_Senpai el cual te notificara cabios en la pagina web y demas cosas que serán de ayuda.'
            '\n'
            '\nEn la página web encontraras más información sobre planes y demás cosas que estare haciendo'
            '\nPreciona el comando /help para saber más'
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🐺Canal🐺', url='https://t.me/keimasenpai')],
            [InlineKeyboardButton(text='⛰X Minecraft', url='https://t.me/x_minecraft_channel')],
            [InlineKeyboardButton(text='📃Página web Personal', url='https://keimasenpaiyt.wordpress.com/')],
            [InlineKeyboardButton(text='🛍Tienda Web ', url='https://vipshopks.wordpress.com/')]
        ])
    )

def xdownloader_command_handler(update, context):
    update.message.reply_text(
        text=(
            '⛰Aquí te dejo la apk XDownoader para cuando la quieras descargar⛰.'
            '\nVe y preciona el botón de descarga que esperas'

        ),

        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='📱XDownloader v1.3.5📱', url='https://t.me/xdownloader_archive/58')],
            [InlineKeyboardButton(text='🖥XDownloader v1.3.5🖥', url='https://t.me/xdownloader_archive/60')],
            [InlineKeyboardButton(text='📦XDownloader Archiver📦', url='https://t.me/xdownloader_archive')]
        ])
    )

   
    
def help_command(update, context):
    id_usuario = update.effective_user['id']
    texto_ayuda = '*👩🏻‍💻Hola este es el bot [Keima Senpai](https://t.me/keimasenpai)👩🏻‍💻*'+'\n\n\n'
    texto_ayuda+= '*👨🏻‍🏫Los comandos son los siguientes*:'+'\n\n'
    texto_ayuda+= '`/xdownloader` Este comando sirve para obtener los link de descarga de la app'+'\n\n'
    texto_ayuda+= '`/sugerir texto` Con este comando envia un problema o pedido al creador del bot'+'\n\n'
    texto_ayuda+= '`/id` Este comando te da tu id de usuario'+'\n\n'
    texto_ayuda+= '`/chanel` Te muestra una lista de Canales exclusivos'+'\n\n'
    texto_ayuda+= '*Ya con esto es suficiente*'+'\n'
    context.bot.sendMessage(chat_id=id_usuario, text=texto_ayuda, parse_mode="MarkdownV2", disable_web_page_preview=True)


def report_problem(update, context):
        text = update.message.text
        name = update.effective_user['first_name']
        user_name = update.effective_user['username']

        if update.message.text == '/sugerir':
            context.bot.send_message(
                chat_id='1618347551',
                text=str(text).replace('/sugerir', f'Nombre: {name}\nNombre de usuario: @{user_name}\n')
            ),



            update.message.reply_chat_action(ChatAction.TYPING)
            time.sleep(3)
            update.message.reply_text(

                text=(
                    '✅Se envío satisfactoriamente la sugerencia✅\n\n'
                    f'{name} no se preocupe el admin lo soluciona en minutos o en caso de ser pedido vip lo contacta enseguida'
                )
            ) 

def id_user(update, context):
    id_usuario = update.effective_user['id']
    context.bot.sendMessage(chat_id= id_usuario, 
    parse_mode="MarkdownV2", 
    text=f'*Su id es*: `{id_usuario}`'
    
    
    )


def chanel_exclusive(update, context):
    id_usuario = update.effective_user['id']
    links_chanel = '*🎴Lista de Canales más buscados en Telegram🎴*'+'\n\n'
    links_chanel+= '*[X Anime ®](https://t.me/x_anime_channel)*'+'\n'
    links_chanel+= '*[X Minecraft ®](https://t.me/x_minecraft_channel)*'+'\n'
    links_chanel+= '*[X Minecraft Archive ®](https://t.me/x_minecraft_archive)*'+'\n'
    links_chanel+= '*[X Wallpapers ®](https://t.me/+SMcLzJhMEwJlZGNh)*'+'\n'
    links_chanel+= '*[X Twitch ®](https://t.me/x_twitch_channel)*'+'\n'
    links_chanel+= '*[🛍️ X Shop VIP ®](https://t.me/shop_vip_shannel)*'+'\n'
    context.bot.sendMessage(chat_id=id_usuario, text=links_chanel, parse_mode="MarkdownV2", disable_web_page_preview=True)

    

if __name__ == '__main__':
    
    token = os.environ['TELEGRAM_TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('xdownloader', xdownloader_command_handler))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('id', id_user))
    dp.add_handler(CommandHandler('chanel', chanel_exclusive))
    dp.add_handler(MessageHandler(filters=Filters.text, callback=report_problem))
    

    updater.start_polling()
    updater.idle()

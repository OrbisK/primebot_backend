from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from communication_interfaces.languages.de_DE import YES, NO


def boolean_keyboard(callback_data_prefix: int):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            YES,
            callback_data=f"{callback_data_prefix}yes"
        )],
        [InlineKeyboardButton(
            NO,
            callback_data=f"{callback_data_prefix}no"
        )],
    ])
    return reply_markup
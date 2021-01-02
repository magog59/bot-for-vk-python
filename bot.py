# V.3
# @link(https://vk.com/magog59) Основатель кода и его изобрёл.
import os,sys
sys.path.append('/home/m/magogsterb/tutorial-env/lib64/python3.4/site-packages/')
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re
import datetime
import requests
from bs4 import BeautifulSoup as BS

vk_session = VkApi(token='токен')
vk = vk_session.get_api()

vk.messages.send(
	chat_id = 4,
	message = "Ваше сообщение или та же переменная.",
	random_id = get_random_id(),
)
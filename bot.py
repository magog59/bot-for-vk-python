from vk_api import VkApi
from vk_api.utils import get_random_id

vk_session = VkApi(token='токен')
vk = vk_session.get_api()

vk.messages.send(
	chat_id = 4,
	message = "Ваше сообщение или та же переменная.",
	random_id = get_random_id(),
)

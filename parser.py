from bs4 import BeautifulSoup
import requests
import itertools
import asyncio
import time


url = 'https://www.avito.ru/all?cd=1&f=ASgCAgECAUXGmgwUeyJmcm9tIjo3MDAwLCJ0byI6MH0&q=колонка+яндекс+миди&s=104'
#url = 'https://www.avito.ru/'
#url = 'https://www.avito.ru/barnaul/zhivotnye'

"""
try:
    response = requests.get(url, timeout=5)  # Добавляем таймаут в 5 секунд
    response.raise_for_status()  # Проверяем статус-код, если ошибка, поднимет исключение
    print("Запрос успешен!")
    #print(response.text)
except requests.exceptions.RequestException as e:  # Обрабатываем все возможные ошибки requests
    print(f"Произошла ошибка: {e}")
except requests.exceptions.Timeout:
    print("Превышено время ожидания запроса")
except requests.exceptions.TooManyRedirects:
    print("Слишком много редиректов")
except requests.exceptions.HTTPError as e:
    print(f"HTTP ошибка: {e}")
except requests.exceptions.ConnectionError:
    print("Ошибка подключения, проверьте интернет соединение")
"""
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


async def main_parser (soup) :
    # получение 1 заказа с сайта
    for card in soup.find_all('div', class_="iva-item-root-Se7z4 photo-slider-slider-ZccM3 iva-item-gallery-nEww5 iva-item-redesign-H4ow9 iva-item-responsive-GCo6h items-item-Reit3 items-galleryItem-lV5TC js-catalog-item-enum"): #получение 1 заказа с сайта
        print("dostup poluchen")
        card_name_tag = card.find('a', class_ = 'styles-module-root-m3BML styles-module-root_noVisited-HHF0s')#.text.strip()    # Находим тег <a>
        if card_name_tag is not None:
            card_name = card_name_tag.get('title') # Извлекаем значение атрибута title
        else:
            card_name = 'Название не найдено'

        card_price_tag =card.find('strong', class_="styles-module-root-LEIrw")
        card_price_span = card_price_tag .find('span')  # Извлекаем значение тега span
        card_price = card_price_span.text.replace('\xa0', '').strip()

        card_link_tag = card.find('a', class_ = 'styles-module-root-m3BML styles-module-root_noVisited-HHF0s')  # Находим тег <a>
        card_link = card_link_tag.get('href')  # Извлекаем значение атрибута href

        card_description_tag = card.find('meta', itemprop='description' )
        if card_description_tag:
            card_description = card_description_tag.get('content')
            print(f"Описание: {card_description}")
        else:
            print("Описание не найдено.")
        #card_description = card_description_tag.get('content')

        print(card_name)
        print(card_price)
        #print(card_description)
        print("link -> https://www.avito.ru"+card_link)
        print("------------------------------------")

        time.sleep(6000) #между парсингами 10 минут интервал




#async def print_order():
  #  return ([order_name,str(order_price),order_link,description])

#async def start_parser(message):
    #await parsing(soup, message)
    #await asyncio.sleep(1)  # Задержка на 30 секунд


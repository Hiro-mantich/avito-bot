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

soup = BeautifulSoup(response.text, 'html.parser')

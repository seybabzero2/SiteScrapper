import requests
from bs4 import BeautifulSoup
import re

emails = []

def find_emails(url):
    try:
        # Отправляем GET-запрос к веб-сайту
        response = requests.get(url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим все текстовые элементы на странице
            text_elements = soup.find_all(text=True)

            # Используем регулярное выражение для поиска электронных адресов
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
            emails = set()

            # Итерируем по текстовым элементам и ищем электронные адреса
            for text in text_elements:
                matches = re.findall(email_pattern, text)
                emails.update(matches)

            return emails
        else:
            print(f"Ошибка при запросе {url}: {response.status_code}")
            return None

    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Список сайтов для проверки
urls = ['http://google.com']

for url in urls:
    found_emails = find_emails(url)

    if found_emails:
        print(f"Найденные электронные адреса на сайте {url}:")
        for email in found_emails:
            print(email)
            emails.append(email)
    else:
        print(f"Не удалось найти электронные адреса на сайте {url}.")

print("\nE-Mails:\n" + "-"*50)
for i in range(len(emails)):
    print(emails[i])

#
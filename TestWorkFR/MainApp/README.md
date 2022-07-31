Шаги к запуску прграмы:

1. В терминале указываем рабочую деректорию командой: cd C:\Users\ruslan\PycharmProjects\TestWorkFR\MainApp  (В моем случае)
2. Далее в терминале пишим: python manage.py makemigrations
3. Далее: python manage.py migrate
4. Создаем суперпользователя(для админки): python manage.py createsuperuser
5. Запускаем сервис: python manage.py runserver

Документация по API:
1. http://127.0.0.1:8000/api/v1/client Добавление нового клиента
2. http://127.0.0.1:8000/clientall Список всех клиентов
3. http://127.0.0.1:8000/detail/<int:pk>/ Обновление данных,удаление определенного пользователя "Вместо int:pk пишем id созданного пользователя!"
4. http://127.0.0.1:8000/api/v1/newsletter Добовление рассылки
5. http://127.0.0.1:8000/detail/newsletter/ Список всех рассылок
6. http://127.0.0.1:8000/detail/put_newsletter/<int:pk> Обновление,удаление рассылки "Вместо int:pk пишем id рассылки"
7. http://127.0.0.1:8000/detail/message/ Список всех сообщений
8. http://127.0.0.1:8000/api/v1/send_message/ Создание/Отправка сообщения
9. http://127.0.0.1:8000/detail/message/<int:pk> Обновление,удаление сообщения "Вместо int:pk пишем id сообщения"
10. http://127.0.0.1:8000/admin Дефолтная Django admin





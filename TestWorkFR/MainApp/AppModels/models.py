from django.db import models


class Newsletter(models.Model):
    id: int = models.IntegerField('id', primary_key=True, null=False, unique=True)
    date = models.DateTimeField('Дата начала рассылки')
    messenge = models.CharField('Текст рассылки', max_length=255)
    phone_operator = models.CharField('Мобильный оператор', max_length=3, null=False)
    date_end = models.DateTimeField('Дата конца рассылки')

    def __str__(self) -> str:
        info = self.id, self.messenge, self.date
        for item in info:
            info = item
        return str(info)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    id: int = models.IntegerField('id', primary_key=True, null=False, unique=True)
    phone_number = models.CharField('Номер телефона', max_length=10, null=False, unique=True)
    phone_operator = models.CharField('Мобильный оператор', max_length=3, null=False)
    tag = models.CharField('Метка', max_length=25)
    Timezone = models.DateTimeField('Часовой пояс')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        info = self.id, self.phone_number, self.tag
        for item in info:
            info = item
        return str(info)


class Message(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    date = models.DateTimeField('Дата отправки сообщения')
    status = models.CharField('Статус', max_length=25)
    id_Newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    id_Сlient = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self) -> str:
        info = self.id, self.status, self.date, self.id_Newsletter, self.id_Сlient
        for item in info:
            info = item
        return str(info)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

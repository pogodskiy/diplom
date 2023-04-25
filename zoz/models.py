from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    username = models.CharField(max_length=20, unique=True, verbose_name='Ник')
    email = models.EmailField(unique=True, verbose_name='@mail')
    password = models.CharField(max_length=15, verbose_name='Пароль')
    customer = models.BooleanField(default=False)

class Products(models.Model):
    cat = models.ForeignKey('CatItems', on_delete=models.PROTECT)
    item_name = models.CharField(max_length=20, unique=True)
    item_detail = models.TextField(max_length=200)
    discount = models.CharField(choices=[('40', '40'), ('30', '30'), ('20', '20'), ('10', '10'), ('No', 'No')])
    comment = models.TextField(max_length=100)
    customer = models.ForeignKey('UserModel', on_delete=models.PROTECT, limit_choices_to={'customer': True}, verbose_name='Поставщик')


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    post_body = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Автор')
    comments = models.CharField
    date = models.TimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title


class CatProduct(models.Model):
    cat_name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.cat_name







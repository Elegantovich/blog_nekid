from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Логин'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    tittle = models.CharField(
        max_length=100,
        verbose_name='Название блога'
    )
    about_blog = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='О блоге'
    )

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.TextField(
        max_length=100,
        verbose_name='Заголовок'
        )
    text = models.TextField(
        help_text='Текст нового поста',
        verbose_name='Текст поста'
        )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата cоздания поста'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
        related_name="posts"
        )

    class Meta():
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Подсписчик',
        related_name='follower'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
        related_name='following'
        )


class Viewed(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь',
        related_name='reader'
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пост',
        related_name='read_post'
        )

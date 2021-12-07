<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/logo1.gif"></p>

# blog_nekid

### Description
Start version of site-blog.

### Tech
Python 3.9, Django 3.2

### How to start a project:

Clone and move to another repository:

```
git clone https://github.com/Elegantovich/blog_nekid/
```

```
cd blog_nekid
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from file requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate 
```

Run the project:

```
python manage.py runserver
```


| Description | URL |
| ------ | ------ |
| /admin/ | / admin zone /
| index | / |
| follow index | /follow/ |
| blog username | /blog/<str:username>/ |
| blog follow | /blog/<str:username>/follow/ |
| blog unfollow | /blog/<str:username>/unfollow/ |
| post detail | /posts/<int:post_id>/ |
| create post | /create/ |
| edit posts | /posts/<int:post_id>/edit/ |
| viewed post | /posts/<int:post_id>/viewed/ |
| unviewed post | /posts/<int:post_id>/unviewed/ |

Сайт представлен в виде бетта версии блога, в которым отсутствует возможность регистрации. Заходить следует с аккаунта суперадмина 
```
/admin/ login "admin2"  password "qwerty123"
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid2.JPG"></p>
В проекте присутствует еще несколько пользователей. На данный аккаунт подписаны User2 и User3, а сам пользователь подписан на все что можно. Посты избранных блогеров отображаются во вкладке "Избранное"
```
/follow/
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid3.JPG"></p>
Подписаться или отписаться на автора можно на странице блога
```
/blog/<str:username>/follow/
```
```
/blog/<str:username>/unfollow/
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid4.JPG"></p>
Посты можно отмечать прочитанными на странице поста
```
/posts/<int:post_id>/viewed/
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid5.JPG"></p>
При добавлении поста автором, подписчики получат уведомление на почту.
```
/create/
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid6.JPG"></p>
Данный пост можно в дальнейшем редактировать
```
/posts/<int:post_id>/edit/
```
<p align="center"><img src="https://github.com/Elegantovich/blog_nekid/blob/Elegantovich/blog_nekid/static/img/nekid7.JPG"></p>
Реализация почтовых сообщений происходит через Django модуль 'django.core.mail.backends.filebased.EmailBackend'.
Письма хранятся в папке /sent_emails в директории blog_nekid.

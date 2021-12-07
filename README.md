
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
| /admin/ | admin zone /
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

Сайт представлен в виде бетта версии блога, в которым отсутсвует возможность регистрации. Заходить следует с аккаунта суперадмина 
```
login "admin2"  password "qwerty123"
```
В проекте присуствует еще несколько пользователей. На данный аккаунт подписаны User2 и User3, а сам пользователь подписан на все что можно. Посты избранных блогеров отображаются во вкладке "Избранное"
```
follow index | /follow/
```
Подписаться или отписаться на автора можно на странице блога
```
blog follow | /blog/<str:username>/follow/
```
```
blog unfollow | /blog/<str:username>/unfollow/
```

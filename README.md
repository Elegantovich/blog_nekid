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
| index | / |
| follow index | /follow/ |
| blog username | /blog/<str:username>/ |
| blog follow | /blog/<str:username>/follow/ |
| blog unfollow | /blog/<str:username>/follow/ |
| post detail | /posts/<int:post_id>/ |
| create post | /create/ |
| edit posts | /posts/<int:post_id>/edit/] |
| viewed post | /posts/<int:post_id>/viewed/ |
| unviewed post | /posts/<int:post_id>/unviewed/ |

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
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

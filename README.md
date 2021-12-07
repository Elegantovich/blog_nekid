[![CI](https://github.com/deadbit-dev/api_yamdb/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/deadbit-dev/api_yamdb/actions/workflows/python-app.yml)

### How to start a project:

Clone and move to another repository:

```
git clone https://github.com/deadbit-dev/api_yamdb.git
```

```
cd api_yamdb
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
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

Run the project:

```
python3 manage.py runserver
```

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |
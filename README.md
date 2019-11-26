## pytest-django-dotenv
Pytest plugin used to specify dotenv for your tests. This project uses
django-dotenv to load your environment variables from your dotenv file.

### Installation
```
pip install pytest-django-dotenv
```

### Setup
Base setup uses `.env` file which is placed equally with virtual environment
directory. If you want to change that behavior you have to add `env_path` to your
`pytest.ini` file which allow you to change path to dotenv file starting from
parent of virtualenv directory.

Example:
If we have virtualenv i `a` directory and dotenv file is placed in parent of `a`
directory then you should add this to your `pytest.ini` file.

```
[pytest]
env_path = 
    ../.env
```

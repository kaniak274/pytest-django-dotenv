import os
import dotenv
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    virtual_env_path = os.getenv('VIRTUAL_ENV')
    dotenv.read_dotenv(os.path.join(virtual_env_path, '../.env'))


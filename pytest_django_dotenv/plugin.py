import os
import dotenv
import pytest


def pytest_addoption(parser):
    parser.addini(
        "env_path",
        type="linelist",
        help="path to .env from $VIRTUAL_ENV",
        default=['.env']
    )

@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    virtual_env_path = os.getenv('VIRTUAL_ENV')
    dotenv.read_dotenv(os.path.join(virtual_env_path, f'../{early_config.getini("env_path")[0]}'))


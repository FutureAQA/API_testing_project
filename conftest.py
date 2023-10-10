import pytest
from pages.base_page import BasePage

base = BasePage()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """
    Calling a function to clear the contents of the logs folder before starting a session
    """
    base.cleanup_folder()

import pytest
from pages.folder_management import FolderManagement

folder_management = FolderManagement()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """
    Calling a function to clear the contents of the logs folder before starting a session
    """
    folder_management.cleanup_folder()


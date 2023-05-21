import pytest
from pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")


@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser


@pytest.fixture()
def open_home_all_browsers(all_browsers):
    home_page = HomePage(browser=all_browsers)
    yield home_page
    home_page.close()


@pytest.fixture()
def open_home(choose_browser):
    home_page = HomePage(browser=choose_browser)
    yield home_page
    home_page.close()

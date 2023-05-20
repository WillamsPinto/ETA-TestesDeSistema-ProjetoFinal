import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")


@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser


@pytest.fixture()
def open_home_all_browsers(all_browsers):
    print("open_home")
    home_page = HomePage(browser=all_browsers)
    yield home_page
    print("close home")
    home_page.close()


@pytest.fixture()
def open_home(choose_browser):
    print("open_home")
    home_page = HomePage(browser=choose_browser)
    yield home_page
    print("close home")
    home_page.close()


@pytest.fixture()
def efetuar_login(open_login):
    print("efetuar login")
    open_login.efetuar_login()
    yield open_login


@pytest.fixture()
def efetuar_login_all_browsers(open_login_all_browsers):
    print("efetuar login")
    open_login_all_browsers.efetuar_login()
    yield open_login_all_browsers

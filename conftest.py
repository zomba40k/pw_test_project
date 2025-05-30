import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
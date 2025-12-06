from playwright.sync_api import Page, sync_playwright
import pytest
from test_dumhudby import page
import requests

def test_status():
    response = requests.get("https://www.dumhudby.cz/")
    assert response.status_code == 200


def test_accept_cookies(page: Page):
    page.goto("https://www.dumhudby.cz/")
    accept_button = page.locator("body > div.cookie-line > button")
    accept_button.click()
    cookie_line = page.locator("body > div.cookie-line")
    assert cookie_line.is_visible() == False
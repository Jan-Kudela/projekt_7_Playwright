from playwright.sync_api import Page, sync_playwright
import pytest
import requests

@pytest.fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo= 1000)
        page = browser.new_page()
        yield page
        browser.close()


def accept_cookies(page: Page):

    accept_button = page.locator("body > div.cookie-line > button")
    accept_button.click()

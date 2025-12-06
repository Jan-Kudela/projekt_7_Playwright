from playwright.sync_api import Page, sync_playwright
import pytest
import time
from test_dumhudby import page, accept_cookies


def generate_email():
    """vrací unikátní email - časové razítko"""
    return f"test_{int(time.time())}@testmail.cz"


def test_new_registration(page: Page):
    email = generate_email()
    page.goto("https://www.dumhudby.cz/")
    accept_cookies(page)
    page.locator("a.user-anchor").click() #prihlasit se button
    page.locator("a.btn.btn-big.btn-second.btn-wide.mtop10").click()
     # nová registrace button
    page.locator("#email").fill(f"{email}") #email
    page.locator("#pwd_reg").fill("motyl55") #password
    page.locator("#pwd1").fill("motyl55") #password2
    page.locator("#name").fill("Jan")
    page.locator("#surname").fill("Novák")
    page.locator("#phone").fill("+420608888555")
    page.locator("#street").fill("Horní 666")
    page.locator("#city").fill("České Budějovice")
    page.locator("#zip").fill("74755")
    page.locator("#content > main > form > div.buttons > input").click()
    #submit button
    assert page.url == "https://www.dumhudby.cz/registration.php?action=reg_ok"


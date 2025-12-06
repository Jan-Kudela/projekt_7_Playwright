from playwright.sync_api import Page, sync_playwright
import pytest
from test_dumhudby import page, accept_cookies


def test_new_registration(page: Page):
    
    page.goto("https://www.dumhudby.cz/")
    accept_cookies(page)
    prihlasit_se_button = page.locator("a.user-anchor")
    prihlasit_se_button.click()
    nova_reg_button = page.locator("a.btn.btn-big.btn-second.btn-wide.mtop10")
    nova_reg_button.click()
    email_fill = page.locator("#email")
    email_fill.fill("jaann@gmail.com")
    password = page.locator("#pwd_reg")
    password.fill("motyl55")
    password_2 = page.locator("#pwd1")
    password_2.fill("motyl55")
    name = page.locator("#name")
    name.fill("Jan")
    surname = page.locator("#surname")
    surname.fill("Novák")
    phone = page.locator("#phone")
    phone.fill("+420608888555")
    street = page.locator("#street")
    street.fill("Horní 666")
    city = page.locator("#city")
    city.fill("České Budějovice")
    zip = page.locator("#zip")
    zip.fill("74755")
    submit_button = page.locator("#content > main > form > div.buttons > input")
    submit_button.click()
    page.pause()
    registration_ok = page.locator("#registrace_ok > span")
    assert page.url == "https://www.dumhudby.cz/registration.php?action=reg_ok"


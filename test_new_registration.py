from playwright.sync_api import Page, sync_playwright
import pytest
from test_dumhudby import page, accept_cookies


def test_new_registration(page: Page):
    
    page.goto("https://www.dumhudby.cz/")
    accept_cookies()
    prihlasit_se_button = page.locator("a.user-anchor")
    prihlasit_se_button.click()
    nova_reg_button = page.locator("a.btn.btn-big.btn-second.btn-wide.mtop10")
    nova_reg_button.click()
    email_fill = page.locator("#email")
    email_fill.fill("jochanan.jorgen@gmail.com")
    password = page.locator("#pwd_reg")
    password.fill("motyl_55.")
    password_2 = page.locator("#pwd_1")
    password_2.fill("motyl_55.")
    #assert cookie_line.is_visible() == False

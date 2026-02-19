from playwright.sync_api import Page, sync_playwright, expect
import pytest
import requests
import time

BASE_URL = "https://www.dumhudby.cz/"

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


def test_status():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_accept_cookies(page: Page):
    page.goto(BASE_URL)
    accept_button = page.locator("body > div.cookie-line > button")
    accept_button.click()
    cookie_line = page.locator("body > div.cookie-line")
    assert cookie_line.is_visible() == False


def generate_email():
    """vrací unikátní email - časové razítko"""
    return f"test_{int(time.time())}@testmail.cz"


def test_new_registration(page: Page):

    # Začne nahrávat před začátkem testu
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    email = generate_email()
    page.goto(BASE_URL)
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

    page.context.tracing.stop(path="trace.zip")

@pytest.mark.sign_in
def test_sign_in_negative(page: Page):
    email = generate_email()
    page.goto(BASE_URL)
    accept_cookies(page)
    page.locator("a.user-anchor").click() #přihlásit se button
    page.locator("input.inp-text[name='email']").fill(f"{email}") #email
    page.locator("#pwd").fill("123456789") #password
    page.locator("input.btn-login").click()
    error_message = page.locator("#content > main > div > p")
    expect(error_message).to_contain_text(
        "Emailová adresa nebo heslo nebylo zadáno správně." \
        " Systém rozlišuje velikost písmen"
        )


horizontal_menu_bar = [
    #{"name": "Home", "url_part": ""},
    {"name": "Kytary", "url_part": "kat-259"},
    {"name": "Struny", "url_part": "kat-907"},
    {"name": "Klávesy", "url_part": "kat-309"},
    #{"name": "Bicí", "url_part": "www.drumcenter.cz"},
    {"name": "Zvuk", "url_part": "kat-310"},
    {"name": "Dechy a smyčce", "url_part": "kat-377"},
    {"name": "Noty a učebnice", "url_part": "kat-460"},
    {"name": "Bazar", "url_part": "view-2845"},
    {"name": "Nové zboží", "url_part": "view-2836"},
    {"name": "Výprodej", "url_part": "view-2841"},
    {"name": "Akce a aktuality", "url_part": "novinka.php?action=views"},
]

@pytest.mark.parametrize("item", horizontal_menu_bar)
def test_horizontal_menu_bar(page,item):
    page.goto(BASE_URL)
    accept_cookies(page)

    page.get_by_role("link", name=item["name"]).first.click()
    assert item["url_part"] in page.url
    


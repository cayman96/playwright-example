import re # podobno nienawidzisz regexów, to jeb - biblioteka do regexów XD
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture()
def main_page(page: Page):
    # bardzo prosty conftest, otwiera nam stronę główną i sprawdza, czy tytuł się zgadza
    page.goto("http://www.kurs-selenium.pl/demo/")
    expect(page).to_have_title(re.compile("PHPTRAVELS"))


import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture()
def mainpage(page: Page):
    page.goto("http://www.kurs-selenium.pl/demo/")
    expect(page).to_have_title(re.compile("PHPTRAVELS"))


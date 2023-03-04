import re
import pytest
from playwright.sync_api import Page, expect


# co zrobiłem, to jako fixture ustawiłem funkcję, która otwiera link na danej stronie -
@pytest.fixture
def mainpage(page: Page):
    page.goto("http://www.kurs-selenium.pl/demo/")
    # pierwsza asercja, wymagany tytuł strony
    expect(page).to_have_title(re.compile("PHPTRAVELS"))
    yield

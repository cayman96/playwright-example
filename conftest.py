import pytest
from playwright.sync_api import Page


# co zrobiłem, to jako fixture ustawiłem funkcję, która otwiera link na danej stronie -
@pytest.fixture
def setup(page: Page):
    page.goto("http://www.kurs-selenium.pl/demo/")
    yield

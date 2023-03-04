# biblioteka do regexów
import re
import pytest
from locators import MainPageLocators
# import Page i expect'a z playwrighta
from playwright.sync_api import Page, expect


# deklaracja funkcji z testu, jako że używamy pytesta to musi się zaczynać od test, tak samo plik się musi tak zaczynać
# a tu oznaczyłem, którego fixture'a ma użyć
@pytest.mark.usefixtures("mainpage")
def test_goto_blog(page: Page):
    # jak używam funkcji get_by_role, to tutaj szukam wg... well, roli elementu, tutaj jest to link,
    # ale może być jako button, text, label, id, i tak dalej... odsyłam do dokumentacji jakby co
    blog_btn = page.locator(MainPageLocators.blogBtn)
    # kolejna asercja - spodziewamy się, że nasz link ma atrybut href o wartości zawierającej /demo/blog
    expect(blog_btn).to_have_attribute("href", re.compile(".*demo/blog"))
    # klik
    blog_btn.click()
    # no i tu sprawdzam, czy
    expect(page).to_have_url(re.compile(".*/demo/blog"))
    expect(page).to_have_title(re.compile("Blog"))

@pytest.mark.usefixtures("mainpage")
def test_goto_offers(page: Page):
    offer_btn = page.locator(MainPageLocators.offersBtn)
    expect(offer_btn).to_have_attribute("href", re.compile(".*/demo/offers"))
    offer_btn.click()
    expect(page).to_have_url(re.compile(".*/demo/offers"))
    expect(page).to_have_title(re.compile("Special Offers"))


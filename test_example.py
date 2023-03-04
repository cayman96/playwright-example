# biblioteka do regexów
import re
import pytest
# import Page i expect'a z playwrighta
from playwright.sync_api import Page, expect


# deklaracja funkcji z testu, jako że używamy pytesta to musi się zaczynać od test, tak samo plik się musi tak zaczynać
# a tu oznaczyłem, którego fixture'a ma użyć
@pytest.mark.usefixtures("setup")
def test_pierwszy_przejdzie(page: Page):
    # pierwsza asercja, wymagany tytuł strony
    expect(page).to_have_title(re.compile("PHPTRAVELS"))
    '''jak używam funkcji get_by_role, to tutaj szukam wg... well, roli elementu, tutaj jest to link,
    ale może być jako button, text, label, id, i tak dalej... odsyłam do dokumentacji jakby co'''
    blog_btn = page.get_by_role("link", name="Blog")
    # kolejna asercja - spodziewamy się, że nasz link ma atrybut href o wartości zawierającej /demo/blog
    expect(blog_btn).to_have_attribute("href", re.compile(".*/demo/blog"))
    # klik
    blog_btn.click()
    # no i tu sprawdzam, czy
    expect(page).to_have_url(re.compile(".*/demo/blog"))


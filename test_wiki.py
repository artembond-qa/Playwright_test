
from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto("https://ru.wikipedia.org/")

    page.get_by_role("link",name="Оборотень").first.click()

    heading = page.get_by_role("heading", name="Сюжет")

    expect(heading).to_be_visible()
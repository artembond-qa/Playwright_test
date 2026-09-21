
from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto("https://ru.wikipedia.org/")

    page.get_by_role("link",name="Нацистская Германия").first.click()

    heading = page.get_by_role("heading", name="Название государства")

    expect(heading).to_be_visible()

def test_add_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")

    todo_input = page.get_by_placeholder("What needs to be done?")

    todo_input.fill("Learn Playwright")
    todo_input.press("Enter")

    todo_item = page.get_by_test_id("todo-item")

    expect(todo_item).to_have_count(1)
    expect(todo_item).to_contain_text("Learn Playwright")
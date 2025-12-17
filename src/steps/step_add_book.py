from playwright.sync_api import expect
from behave import given, when, then

@given(u'user is on the main pages')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout=5000)

@when(u'user clicks on the "Lägg till bok" button')
def step_when_click_add_book_button(context):
    add_book_button = context.page.get_by_test_id("add-book")
    add_book_button.click()

@when("user adds the following books:")
def step_when_add_multiple_books(context):
    context.added_books = []  # store books for later assertions

    for row in context.table:
        title = row["book_title"]
        author = row["book_author"]

        context.added_books.append((title, author))

        context.page.get_by_test_id("add-input-title").click()
        context.page.get_by_test_id("add-input-title").fill(title)

        context.page.get_by_test_id("add-input-author").click()
        context.page.get_by_test_id("add-input-author").fill(author)

        context.page.get_by_test_id("add-submit").click()

@when(u'user clicks on the "Katalog" button')
def step_when_click_catalog_button(context):
    catalog_button = context.page.get_by_test_id("catalog")
    catalog_button.click()

@then(u'the books should appear in the book list')
def step_then_books_in_list(context):
    # TODO Ändra till RegEx
    for title, author in context.added_books:
        book_text = f'"{title}", {author}'

        book = context.page.get_by_text(book_text)
        expect(book).to_be_visible()



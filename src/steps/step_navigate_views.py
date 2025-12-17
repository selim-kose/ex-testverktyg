from playwright.sync_api import expect
from behave import given, when, then
import re

@given(u'user is on the main paige')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout= 5000)

@then(u'user should see the catalog of books')
def step_then_catalog_books_visible(context):
   catalog = context.page.get_by_test_id("catalog")
   expect(catalog).to_be_visible()

   book = context.page.get_by_test_id(re.compile("star-")).first
   expect(book).to_be_visible()
    
@when(u'user klicks on "Lägg till bok"')
def step_when_click_add_book(context):
    add_book_button = context.page.get_by_test_id("add-book")
    add_book_button.click()

@then(u'user should see "Titel" and "Författare" input fields')
def step_then_title_author_labels_visible(context):
    title_input = context.page.get_by_test_id("add-input-title")
    author_input = context.page.get_by_test_id("add-input-author")
    expect(title_input).to_be_visible()
    expect(author_input).to_be_visible()

@when(u'user clicks on "Mina böcker"')
def step_when_click_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()

@then(u'user should see the list of favorite books')
def step_then_favorite_books_visible(context):
    favorite_list = context.page.get_by_role("paragraph").filter(has_text=re.compile("favoritböcker"))
    expect(favorite_list).to_be_visible()

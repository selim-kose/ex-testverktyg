from playwright.sync_api import expect
from behave import given, when, then
import re


@given(u'user is on the main page and marks a book as favorite')
def step_given_start_page_with_favorite(context):
    context.page.goto(context.base_url, timeout=5000)

    # Mark a book as favorite
    heart_icon = context.page.get_by_test_id(re.compile("star-")).first
    heart_icon.click(timeout=1000)
    context.heart_icon = heart_icon
    
    # Get the book title associated with the clicked heart icon for later verification
    parent = heart_icon.locator("..")
    text_title_author = parent.inner_text().replace("❤️", "").strip()
    title = re.match(r'"(.+?)",',text_title_author).group(1)
    #print(title)
    context.selected_title = title

    expect(heart_icon).to_have_class(re.compile("selected"))

@when(u'user clicks on a "Mina böcker" button')
def step_when_click_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()

@then(u'user should see the marked book listed as a favorite')
def step_then_see_favorite_book(context):
    favorite_book = context.page.get_by_text(context.selected_title)
    expect(favorite_book).to_be_visible()

@when(u'user clicks on "Katalog" button')
def step_when_click_catalog_button(context):
    catalog_button = context.page.get_by_test_id("catalog")
    catalog_button.click()

@when(u'user clicks on the filled heart icon next to a book title')
def step_when_click_filled_heart_icon(context):
    heart_icon = context.heart_icon
    heart_icon.click(timeout=1000)

@then(u'the heart icon should be removed, indicating the book is unmarked as favorite')
def step_then_heart_icon_unfilled(context):
    expect(context.heart_icon).not_to_have_class(re.compile("selected"))

@when(u'user clicks on "Mina böcker" button again')
def step_when_click_my_books_again(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()

@then(u'user should not see the book listed as a favorite anymore')
def step_then_not_see_favorite_book(context):
    favorite_book = context.page.get_by_text(context.selected_title)
    expect(favorite_book).not_to_be_visible()
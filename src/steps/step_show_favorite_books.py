from playwright.sync_api import expect
from behave import given, when, then
import re


@given(u'user is on the main paige and no books is marked as favorite')
def step_given_start_page_with_no_favorite(context):
    context.page.goto(context.base_url, timeout=5000)
    hearts = context.page.get_by_test_id(re.compile("star-"))
    count = hearts.count()
    
    #Loop through all heart icons and ensure none are selected
    for i in range(count):
        heart = hearts.nth(i)
        expect(heart).not_to_have_class(re.compile("selected"))

@when(u'user klicks on heart icon next to a book title')
def step_when_click_heart_icon(context):
    heart_icon = context.page.get_by_test_id(re.compile("star-")).first
    heart_icon.click()

    context.heart_icon = heart_icon

    # Get the book title associated with the clicked heart icon for later verification
    parent = heart_icon.locator("..")
    text_title_author = parent.inner_text().replace("❤️", "").strip()
    title = re.match(r'"(.+?)",',text_title_author).group(1)
    #print(title)
    context.selected_title = title

@then(u'the heart should be filled, indicating the book is marked as favorite')
def step_then_heart_icon_filled(context):
    heart_icon = context.heart_icon
    expect(heart_icon).to_have_class(re.compile("selected"))

@when(u'user clicks on "Mina böcker" button')
def step_when_click_my_books(context):
    my_books_button = context.page.get_by_test_id("favorites")
    my_books_button.click()

@then(u'user should see the book listed as a favorite')
def step_then_see_favorite_book(context):
    favorite_book = context.page.get_by_text(context.selected_title)
    expect(favorite_book).to_be_visible()

    
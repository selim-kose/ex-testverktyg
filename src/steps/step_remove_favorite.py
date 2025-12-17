from playwright.sync_api import expect
from behave import given, when, then
import re

@given(u'user is on the main page and a book is marked as favorite')
def step_given_start_page_with_favorite(context):
    context.page.goto(context.base_url, timeout=5000)

    # Mark a book as favorite
    heart_icon = context.page.get_by_test_id(re.compile("star-")).first
    heart_icon.click(timeout=1000)
    context.heart_icon = heart_icon
    expect(heart_icon).to_have_class(re.compile("selected"))

@when(u'user clicks on a filled heart icon next to a book title')
def step_when_click_filled_heart_icon(context):
    heart_icon = context.heart_icon
    heart_icon.click(timeout=1000)

@then(u'the heart icon should be unfilled, indicating the book is unmarked as favorite')
def step_then_heart_icon_unfilled(context):
    expect(context.heart_icon).not_to_have_class(re.compile("selected"))
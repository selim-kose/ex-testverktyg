import re

from playwright.sync_api import expect
from behave import given, when, then

@given(u'user is on the main page')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout=5000)

@when(u'user clicks on a heart icon next to a book title')
def step_when_click_heart_icon(context):
    heart_icon = context.page.get_by_test_id("star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen")
    heart_icon.click()

    context.heart_icon = heart_icon
    
    #context.page.wait_for_timeout(500)  # Wait for the UI to update

@then(u'the heart icon should be filled, indicating the book is marked as favorite')
def step_then_heart_icon_filled(context):
    print(context.heart_icon.get_attribute("class"))
    expect(context.heart_icon).to_have_class(re.compile("selected"))

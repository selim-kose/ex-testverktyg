from playwright.sync_api import expect
from behave import given, when, then
import re

@given(u'users is on the main paige')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout=5000)

@when(u'user hovers over a book title')
def step_when_hover_book_title(context):
    first_heart = context.page.get_by_test_id(re.compile("star-")).first
    first_heart.hover()

@then(u'the favorite heart icon should appear transparent')
def step_then_heart_icon_transparent(context):
    heart_icon = context.page.get_by_test_id(re.compile("star-")).first
    expect(heart_icon).to_have_css("opacity", "0.65")
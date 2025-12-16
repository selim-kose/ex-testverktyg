import re

from playwright.sync_api import expect
from behave import given, when, then

@given(u'user is on the main page')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout=5000)
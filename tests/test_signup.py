from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_signup(page):
    page = logged_in_context.new_page()
    page.goto(CONF.BASE_URL)
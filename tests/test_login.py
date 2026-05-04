from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_check_loging(logged_in_context):
    page = logged_in_context.new_page()
    page.goto(CONF.BASE_URL)
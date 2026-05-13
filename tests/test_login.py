from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_check_loging(logged_in_context):
    page = logged_in_context
    # page.goto(CONF.BASE_URL)


# def test_check_loging(logged_in_context):
#     page = logged_in_context.pages[0]
#     page.wait_for_timeout(5000)
#     subscribe_btn = page.locator("#quotaLimitReached")
#     expect(subscribe_btn).to_be_visible(timeout=10000)
#     subscribe_btn.click()
#     # page.wait_for_url("**/AdvocateProfileMyAccount")
#     page.screenshot(path="logged_in.png")
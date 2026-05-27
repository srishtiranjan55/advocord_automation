import re

from playwright.sync_api import expect


def test_check_login(logged_in_page):
    expect(logged_in_page).to_have_url(re.compile(r".*/dashboard.*"), timeout=60000)


# def test_check_loging(logged_in_context):
#     page = logged_in_context.pages[0]
#     page.wait_for_timeout(5000)
#     subscribe_btn = page.locator("#quotaLimitReached")
#     expect(subscribe_btn).to_be_visible(timeout=10000)
#     subscribe_btn.click()
#     # page.wait_for_url("**/AdvocateProfileMyAccount")
#     page.screenshot(path="logged_in.png")

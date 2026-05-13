from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_delete_folder(logged_in_context):
    page = logged_in_context.pages[0]
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.wait_for_timeout(5000)

    folder = page.locator("text=eye.jpg").first
    folder.click()
    page.wait_for_timeout(2000)

    page.locator("#documentDelete").click()
    page.wait_for_timeout(2000)
    page.locator("#DeleteButton").click()

    page.wait_for_timeout(3000)
    expect(folder).not_to_be_visible(timeout=10000)
    page.wait_for_timeout(10000)
    page.screenshot(path="delete_success.png", full_page=True)

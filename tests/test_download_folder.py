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

    with page.expect_popup() as popup_info:
        page.locator("#documentDownload").click()

    new_page = popup_info.value
    new_page.wait_for_load_state()
    page.wait_for_timeout(5000)
    new_page.screenshot(path="download_page.png", full_page=True)



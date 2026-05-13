from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_create_folder(logged_in_context):
    page = logged_in_context.pages[0]
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()

    page.locator("#fileUploadModal").set_input_files(
        r"C:\Users\ranja\Downloads\eye.jpg"
    )
    page.wait_for_timeout(10000)
    page.screenshot(path="upload_success.png", full_page=True)


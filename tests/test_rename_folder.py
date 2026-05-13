from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_delete_folder(logged_in_context):
    page = logged_in_context.pages[0]
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.wait_for_timeout(5000)

    folder = page.locator("text=eye.jpg").first
    folder.click(button="right", force=True)
    page.wait_for_timeout(2000)
    page.get_by_text("Rename", exact=True).click()
    page.wait_for_timeout(2000)

    rename_input = page.locator("#folderName")
    expect(rename_input).to_be_visible()
    rename_input.fill("eye.jpg")
    page.wait_for_timeout(2000)

    page.locator("#documentPopUpRename").click()
    page.wait_for_timeout(5000)
    page.screenshot(path="rename_success.png", full_page=True)


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
    page.get_by_text("Move to", exact=True).click()
    page.wait_for_timeout(2000)

    # page.get_by_text("Srishti").click()
    # page.wait_for_timeout(2000)

    destination_folder = page.locator("text=Srishti").last
    destination_folder.scroll_into_view_if_needed()
    destination_folder.click()

    page.locator("#documentMove").click()
    page.wait_for_timeout(5000)
    page.screenshot(path="moveto_success.png", full_page=True)

    # page.locator("#moveFileButton").click()
    # page.wait_for_timeout(5000)

    # move_btn = page.get_by_role("button", name="Move")

    # expect(move_btn).to_be_visible()
    # expect(move_btn).to_be_enabled()
    # move_btn.click()


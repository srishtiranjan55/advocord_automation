from playwright.sync_api import expect

def test_download_folder(logged_in_page):
    page = logged_in_page
    page.wait_for_timeout(5000)
    page.locator(".depedentArrowCircle").click()
    page.wait_for_timeout(5000)
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
    new_page.screenshot(path="reports/screenshots/download_page.png", full_page=True)



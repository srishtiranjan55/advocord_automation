from playwright.sync_api import expect


def test_upload_file(logged_in_page):
    page = logged_in_page
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()

    page.locator("#fileUploadModal").set_input_files(
        r"C:\Users\ranja\Downloads\eye.jpg"
    )
    page.wait_for_timeout(10000)
    page.screenshot(path="reports/screenshots/upload_success.png", full_page=True)


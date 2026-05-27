from playwright.sync_api import expect


def test_delete_folder(logged_in_page):
    page = logged_in_page
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.wait_for_timeout(5000)
    
    # page.set_input_files(
    # "input[type='file']",
    # "tests/test_data/ice.jpg"
    # )
    # folder = page.locator("text=ice.jpg").first
    # folder.click()

    file_input = page.locator("input[type='file']")
    file_input.wait_for(state="attached", timeout=60000)

    file_input.set_input_files("tests/test_data/ice.jpg")

    page.locator("#documentDelete").click()
    page.wait_for_timeout(2000)
    page.locator("#DeleteButton").click()

    page.wait_for_timeout(3000)
    expect(folder).not_to_be_visible(timeout=10000)
    page.wait_for_timeout(10000)
    page.screenshot(path="reports/screenshots/delete_success.png", full_page=True)

from playwright.sync_api import expect


def test_rename_folder(logged_in_page):
    page = logged_in_page
    page.locator(".depedentArrowCircle").click()
    page.wait_for_timeout(5000)
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.wait_for_timeout(5000)

    page.set_input_files(
    "input[type='file']",
    "tests/test_data/hills.jpg"
    )

    folder = page.locator("text=hills.jpg").first
    folder.click(button="right", force=True)
    page.wait_for_timeout(2000)
    page.get_by_text("Rename", exact=True).click()
    page.wait_for_timeout(2000)

    rename_input = page.locator("#folderName")
    expect(rename_input).to_be_visible()
    rename_input.fill("abc.jpg")
    page.wait_for_timeout(2000)

    page.locator("#documentPopUpRename").click()
    page.wait_for_timeout(5000)
    page.screenshot(path="reports/screenshots/rename_success.png", full_page=True)


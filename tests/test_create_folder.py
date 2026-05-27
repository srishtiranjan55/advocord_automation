from playwright.sync_api import expect

def test_create_folder(logged_in_page):
    page = logged_in_page
    page.locator(".depedentArrowCircle").click()
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.locator("#documentAdd").click()

    popup_title = page.locator("#documentPopUpRenameTitle")
    expect(popup_title).to_be_visible(timeout=10000)
    expect(popup_title).to_have_text("New Folder")
    
    page.screenshot(path="reports/screenshots/popup_opened.png")

    folder_input = page.locator("#folderName")
    expect(folder_input).to_be_visible()
    folder_input.fill("Srishti")

    page.screenshot(path="reports/screenshots/folder_name_entered.png")

    create_btn = page.locator("#documentPopUpCreate")
    expect(create_btn).to_be_visible()
    create_btn.click()
    page.wait_for_timeout(3000)

    page.screenshot(path="reports/screenshots/folder_created.png")

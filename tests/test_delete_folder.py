from playwright.sync_api import expect

def test_delete_folder(logged_in_page):
    page = logged_in_page
    page.locator(".depedentArrowCircle").click()
    page.wait_for_timeout(5000)
    page.locator(".navDropdownLabel", has_text="Documents").click()
    page.wait_for_timeout(5000)
    
    page.set_input_files(
    "input[type='file']",
    "tests/test_data/ice.jpg"
    )
    folder = page.locator("text=ice.jpg").first
    folder.click()

    page.locator("#documentDelete").click()
    page.wait_for_timeout(2000)
    page.locator("#DeleteButton").click()

    page.wait_for_timeout(3000)
    expect(folder).not_to_be_visible(timeout=10000)
    page.wait_for_timeout(10000)
    page.screenshot(path="reports/screenshots/delete_success.png", full_page=True)

# def test_delete_folder(logged_in_page):
#     page = logged_in_page
#     page.locator(".depedentArrowCircle").click()
#     page.wait_for_timeout(5000)
#     page.locator(".navDropdownLabel", has_text="Documents").click()
#     # page.locator('a[href="/dependent-documents"]').click()
#     page.wait_for_timeout(50000)

    
    
#     # page.wait_for_selector(
#     # ".loader",
#     # state="hidden",
#     # timeout=15000
#     # )

#     page.screenshot(path="check.png", full_page=True)

from playwright.sync_api import expect


def test_move_to_folder(logged_in_page):
    page = logged_in_page
    page.wait_for_timeout(5000)
    page.locator(".depedentArrowCircle").click()
    page.wait_for_timeout(5000)
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
    page.screenshot(path="reports/screenshots/moveto_success.png", full_page=True)



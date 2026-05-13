import pytest
from playwright.sync_api import Browser, BrowserContext, Page, expect
from conf import CONF

@pytest.fixture(scope="session")
def logged_in_context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    page = context.new_page()
    page.goto(CONF.BASE_URL, timeout=60000)
    page.get_by_placeholder("Email").fill(CONF.EMAIL)
    page.get_by_placeholder("Password").fill(CONF.PASSWORD)
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(5000)

    # subscribe_btn = page.locator("#quotaLimitReached")
    # expect(subscribe_btn).to_be_visible(timeout=10000)
    # subscribe_btn.click()

    page.screenshot(path="logged_in.png")

    yield context
    context.close()
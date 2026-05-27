import pytest
import re
from pathlib import Path

from playwright.sync_api import Browser, BrowserContext, Page, expect
from conf import CONF


REPORTS_DIR = Path("reports")
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"


@pytest.fixture(autouse=True)
def _create_report_dirs():
    REPORTS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)


def login(page: Page) -> None:
    page.goto(CONF.BASE_URL, timeout=60000)
    page.get_by_placeholder("Email").fill(CONF.EMAIL)
    page.get_by_placeholder("Password").fill(CONF.PASSWORD)
    page.get_by_role("button", name="Log In").click()

    page.wait_for_url("**/dashboard", timeout=60000)
    expect(page).to_have_url(re.compile(r".*/dashboard.*"), timeout=60000)


@pytest.fixture()
def logged_in_context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    page = context.new_page()
    login(page)

    # subscribe_btn = page.locator("#quotaLimitReached")
    # expect(subscribe_btn).to_be_visible(timeout=10000)
    # subscribe_btn.click()

    page.screenshot(path=SCREENSHOTS_DIR / "logged_in.png")

    yield context
    context.close()


@pytest.fixture()
def logged_in_page(logged_in_context: BrowserContext) -> Page:
    return logged_in_context.pages[0]

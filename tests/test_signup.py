from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_signup(page):
    email = f"anand+186@bluefintechpartners.com"
    # email = f"girish+182@bluefintechpartners.com"
    password = "P@55word"

    page.goto(CONF.BASE_URL, timeout=60000)
    page.locator("#JoinNowButton").click()

    page.locator("#userFirstName").fill("dubey")
    page.locator("#userLastName").fill("saurabh")
    page.locator("#userEmail").fill(email)
    page.locator("#userPassword").fill(password)
    # page.get_by_role("button", name="Create FREE ACCOUNT").click()
    page.locator("#EmailSignUpButton").click()

    page.get_by_placeholder("Enter Code").wait_for(state="visible")
    page.wait_for_function(
        """() => {
            const input = document.querySelector('[placeholder="Enter Code"]');
            return input && input.value.length === 6;
        }""",
        timeout=300000
    )
    page.locator("#UnVerified_Lead").click()
    page.wait_for_url("**/accountVerified")
    expect(page.locator("#Verified_Lead")).to_be_visible()
    page.screenshot(path="signup.png")

    page.locator("#userEmail").fill(email)
    page.locator("input[placeholder='Password']").fill(password)

    page.locator("#Verified_Lead").click()
    page.screenshot(path="signup1.png")

    page.wait_for_url("**/dashboard")
    page.screenshot(path="signup2.png")

    # Popup 1
    expect(page.locator("#Free_Trial")).to_be_visible()
    page.locator("#Free_Trial").click()
    page.screenshot(path="signup3.png")

    # Popup 2
    expect(page.locator("#quickCallContiueButtonId")).to_be_visible()
    page.locator("#quickCallContiueButtonId").click()
    page.screenshot(path="signup4.png")

    # Popup 3
    expect(page.locator("#rolePopUpSkitButton")).to_be_visible()
    page.locator("#rolePopUpSkitButton").click()
    page.screenshot(path="signup5.png")

    # Popup 4
    expect(page.locator("#surveyPopUpSkipButton")).to_be_visible()
    page.locator("#surveyPopUpSkipButton").click()
    page.screenshot(path="signup6.png")




















    
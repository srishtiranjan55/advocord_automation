from playwright.sync_api import expect
from conf import CONF

def test_dynamic_email_signup(page):
    email_number = 186
    password = "P@55word"

    page.goto(CONF.BASE_URL, timeout=60000)
    page.locator("#JoinNowButton").click()

    while True:
        email = f"anand+{email_number}@bluefintechpartners.com"
        page.locator("#userFirstName").fill("dubey")
        page.locator("#userLastName").fill("saurabh")
        page.locator("#userEmail").fill(email)
        page.locator("#userPassword").fill(password)
        page.locator("#EmailSignUpButton").click()

        error_message = page.locator("text=User already exists")
        if error_message.is_visible(timeout=3000):
            email_number += 1
            page.locator("#userEmail").clear()
        else:
            break
    page.screenshot(path="reports/screenshots/dynamic_signup.png")

    # page.get_by_placeholder("Enter Code").wait_for(state="visible")

from playwright.sync_api import expect,Page,BrowserContext
from conf import CONF

def test_payment_method(logged_in_context):
    page = logged_in_context.pages[0]
    page.locator("span.sideBarNavLabel", has_text="Settings").click()
    page.wait_for_load_state("networkidle")
    page.locator("div.dependentTab span", has_text="Payment Method").click()
    page.wait_for_timeout(2000)
    page.locator("span.marginLeft20.cursorPointer").click()

    page.frame_locator('iframe[title*="card number"]') \
    .locator('input[name="cardnumber"]') \
    .fill("4242424242424242")

    page.frame_locator('iframe[title*="expiration"]').locator('input[name="exp-date"]').fill("12/26")
    page.frame_locator('iframe[title*="CVC"]').locator('input[name="cvc"]').fill("123")
    page.locator('input.inputColum24size').fill("GK10")
   
    page.locator('input[value="APPLY"]').click()
    page.wait_for_timeout(2000)

    save_btn = page.locator('input[value="Save"]')
    expect(save_btn).to_be_visible(timeout=10000)
    save_btn.click()
    page.screenshot(path="payment_method.png")

    page.get_by_text("Okay").click(timeout=10000)
    page.screenshot(path="payment_method1.png")


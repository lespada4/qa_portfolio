from playwright.sync_api import sync_playwright

def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com/")
        
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        
        page.wait_for_load_state("networkidle")
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        page.locator(".shopping_cart_link").click()
        
        cart_item = page.locator(".cart_item")
        assert cart_item.is_visible(), "Товар не добавлен в корзину"
        
        # 👇 НОВЫЙ БЛОК КОДА
        page.locator("#checkout").click()
        
        page.locator("#first-name").fill("Test")
        page.locator("#last-name").fill("User")
        page.locator("#postal-code").fill("12345")
        page.locator("#continue").click()
        
        page.wait_for_load_state("networkidle")
        
        page.locator("#finish").click()
        
        success_message = page.locator(".complete-header")
        assert success_message.is_visible(), "Заказ не оформлен"
        assert "Thank you" in success_message.text_content(), "Текст подтверждения не совпадает"
        
        browser.close()
        print("Тест пройден. Заказ оформлен.")
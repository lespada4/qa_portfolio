from playwright.sync_api import sync_playwright

def test_github_open_marzban_repo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://github.com/gozargah/marzban")
        page.wait_for_load_state("networkidle")
        
        code_button = page.locator("button:has-text('Code')")
        assert code_button.is_visible(), "Кнопка 'Code' не найдена"
        
        browser.close()
        print("Тест пройден. Репозиторий открыт, кнопка Code доступна.")
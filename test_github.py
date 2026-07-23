from playwright.sync_api import sync_playwright

def test_github_search_and_open_repo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://github.com/search?q=pytest")
        page.wait_for_load_state("networkidle")
        
        repo_link = page.get_by_text("pytest-dev/pytest", exact=True).first
        repo_link.click()
        
        page.wait_for_load_state("networkidle")
        
        code_button = page.locator("button:has-text('Code')")
        assert code_button.is_visible(), "Кнопка 'Code' не найдена"
        
        browser.close()
        print("Репозиторий открыт, кнопка Code доступна")
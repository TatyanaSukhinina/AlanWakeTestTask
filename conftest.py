import pytest
from news_page import NewsPage
import playwright
from playwright.sync_api import sync_playwright, expect


# Фикстура, которая создает экземпляр NewsPage перед каждым тестом
# и уничтожает его после завершения теста
@pytest.fixture(scope='session')
def news_page():
    with sync_playwright() as playwright:  # Получаем Playwright
        browser = playwright.chromium.launch(headless=False)  # headless=False для визуального наблюдения
        page = browser.new_page()
        page.goto("https://www.alanwake.com/news/#/feed")  # путь HTML-файлу
        page.wait_for_load_state("load")
        yield NewsPage(page)  # Возвращаем экземпляр news_page()
        browser.close()

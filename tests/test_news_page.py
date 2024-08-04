from playwright.sync_api import sync_playwright, expect
import pytest

def test_social_media_links(news_page):
    """Тест проверяет корректность ссылок на социальные сети"""
    # Ожидаемые ссылки на соцсети
    expected_links = {
        'facebook': 'https://facebook.com/alanwake',
        'twitter': 'https://twitter.com/alanwake',
        'instagram': 'https://instagram.com/alanwakeofficial',
        'youtube': 'https://youtube.com/remedygames',
        'discord': 'https://discord.gg/remedygames',
        'tiktok': 'https://www.tiktok.com/@remedy.games'
    }
    actual_links = news_page.get_social_media_links()

    # Если одна или несколько ссылок не совпадают, тест упадет и локализует ошибку
    for social_name, expected_link in expected_links.items():
        actual_link = actual_links.get(social_name)
        if actual_link != expected_link:
            assert False, f"Неверная ссылка для {social_name}: Ожидалось {expected_link}, получено {actual_link}"

    # Если все ссылки верны, то тест пройдет
    assert True, "Все ссылки на соцсети верны"


def test_show_more_button(news_page):
    """Тест проверяет чтобы при нажатии на кнопку "show more" появлялись дополнительные статьи"""
    news_page.accept_all_cookies()
    # Считаем количество статей до нажатия кнопки
    count_articles_before_show_button_click = news_page.count_articles()
    # Нажимаем на кнопку
    news_page.click_show_more()
    # Считаем количество статей после нажатия кнопки
    count_articles_after_show_button_click = news_page.count_articles()
    assert count_articles_before_show_button_click < count_articles_after_show_button_click, "Количество статей не увеличилось"


# Запускаем тесты с помощью pytest
with sync_playwright() as playwright:
    pytest.main(["-v", "-s"])

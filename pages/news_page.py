from playwright.sync_api import Page, expect


class NewsPage:
    def __init__(self, page: Page):
        # Инициализация страницы и локаторов элементов
        self.page = page
        self.accept_all_cookies_button_locator = "#wt-cli-accept-all-btn"
        self.show_more_button_locator = "xpath=//button[@class = 'c-button']"

    def get_social_media_links(self):
        """
        Получает ссылки на все иконки социальных сетей на странице.

        Returns:
            dict: Словарь с названиями соцсетей и ссылками на них.
        """
        social_links = {}
        social_icons = self.page.query_selector_all(".c-social-media-links__list li a")
        for icon in social_icons:
            link = icon.get_attribute('href')
            social_links[icon.get_attribute('aria-label').split()[-1]] = link
        return social_links

    def click_show_more(self):
        """ Нажимает на кнопку 'Show more' """
        self.page.wait_for_selector(self.show_more_button_locator)
        show_more_button = self.page.locator(self.show_more_button_locator)
        show_more_button.scroll_into_view_if_needed()
        show_more_button.click()

    def count_articles(self):
        """
        Подсчитывает количество статей на странице.

        Returns:
            list: Список элементов - статей на странице.
        """
        article_list = self.page.query_selector_all(".l-feed__item")
        return len(article_list)

    def accept_all_cookies(self):
        """ Принимает все cookies, если появилось уведомление """
        accept_all_cookies_button = self.page.locator(self.accept_all_cookies_button_locator)
        if accept_all_cookies_button.is_visible():
            accept_all_cookies_button.click()










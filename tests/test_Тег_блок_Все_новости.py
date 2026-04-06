from testit_python_commons.decorators import externalId, displayName
import time

class TestTagNews:
    @externalId("test_tag_news")
    @displayName("Тег в блоке Все новости")
    def test_tag_news(self, tag_news):
        tag_news.open()
        time.sleep(5)
        print(tag_news.driver.page_source[:3000])
        tag_news.click_tag_news()
   
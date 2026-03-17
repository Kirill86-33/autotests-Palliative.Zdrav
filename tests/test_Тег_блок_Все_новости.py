from testit_python_commons.decorators import externalId, displayName
class TestTagNews:
    @externalId("test_tag_news")
    @displayName("Тег в блоке Все новости")
    def test_tag_news(self, tag_news):  
        tag_news.open()
        tag_news.click_tag_news()
   
import traceback

import requests
from bs4 import BeautifulSoup as bs4
from nlp_processor import Nlp_processor

nlp_processor = Nlp_processor()


class Scraper:
    # 指定したURLからソースを取得(心霊スポット)
    # def get_source_from_url(self, url: str):
    #     SITE_URL:str = 'https://shin-kichi.com/category/spot/'
    #     # sys.setrecursionlimit(10000)
    #     try:
    #         soup = self.get_soup(SITE_URL)
    #         a_elems_for_articles =  soup.find_all('a', class_='st-box-a')
    #         # urls_for_articles=[]
    #         items=[]
    #         if a_elems_for_articles:
    #             for a_elem in a_elems_for_articles:
    #                 href_str = a_elem.attrs['href']
    #                 # urls_for_articles.append(href_str)
    #                 item = {
    #                 'url': href_str
    #                 }
    #                 items.append(item)

    #         # return urls_for_articles

    #         return items

    #     except Exception as excep:
    #         print("Exception\n" + traceback.format_exc())

    #         return None

    # 怖い話投稿サイト「奇々怪々」短編
    async def get_source_from_url(self, url: str):
        SITE_URL: str = "https://kikikaikai.fan/category/scary_story_s"
        try:
            soup = self.get_soup(SITE_URL)
            li_elems_for_articles = soup.find("ul", class_="card-list").find_all("li")
            items = []

            if li_elems_for_articles:
                for li_elem in li_elems_for_articles:
                    a_elem = li_elem.find("a")
                    url_str = a_elem.attrs["href"]
                    title_str = a_elem.attrs["title"]

                    # 各URLからBeautifulSoupを取得
                    __soup_for_article = self.get_soup(url_str)
                    # 本文を取得
                    __text_for_article: str = (
                        __soup_for_article.find(True, class_="main-text")
                        .text.replace("\n", "")
                        .strip()
                    )
                    # 形態素解析
                    tokens = await nlp_processor.morphological_analyzer(
                        __text_for_article
                    )

                    item = {
                        "title": title_str,
                        "url": url_str,
                        "text": __text_for_article,
                        "tokens": tokens,
                    }
                    items.append(item)

            return items

        except Exception as excep:
            print("Exception\n" + traceback.format_exc())

            return None

    # urlからBeautifulSoupを取得
    def get_soup(self, url: str) -> bs4:
        res = requests.get(url)
        soup = bs4(res.content, "lxml")
        return soup

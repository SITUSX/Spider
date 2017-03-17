from Trial import HTML_Downloader
from Trial import HTML_Outputer
from Trial import HTML_Parser
from Trial import URL_Manager


class SpiderMain(object):
    def __init__(self):
        self.urls = URL_Manager.URLManager()
        self.downloader = HTML_Downloader.HTMLDownloader()
        self.parser = HTML_Parser.HTMLParser()
        self.outputer = HTML_Outputer.HTMLOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            # noinspection PyBroadException
            try:
                new_url = self.urls.get_new_url()
                print 'count %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data()

                if count == 1:
                    break
                count = count + 1
            except:
                print 'Craw failed'

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Java"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

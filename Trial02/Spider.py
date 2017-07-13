import urllib
import urllib2
import re
import urlparse


class Spider(object):
    def __init__(self):
        pass

    def HTMLDownload(self, root_url):
        responce = urllib2.urlopen(root_url)
        print ('Code: %d' % (responce.getcode()))

    def HTMLParse(self):
        pass

    def HTMLOutput(self):
        pass

if __name__ == "__main__":
    root_url = "http://219.219.120.48/jiaowu/"
    obj_spider = Spider()
    obj_spider.HTMLDownload(root_url)

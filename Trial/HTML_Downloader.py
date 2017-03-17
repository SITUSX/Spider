import urllib2


class HTMLDownloader(object):
    def download(self, url):
        if url is None:
            return None

        responce = urllib2.urlopen(url)

        if responce.getcode() != 200:
            return None

        return responce.read()

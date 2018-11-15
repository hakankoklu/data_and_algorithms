from datetime import datetime
from urllib import request, error
from threading import Thread


class WebRequests:

    def __init__(self):
        pass

    def ping_website(self, url):
        url, num = url
        try:
            time1 = datetime.utcnow()
            response = request.urlopen(url)
        except error.HTTPError as e:
            print('The server couldn\'t fulfill the request. Reason:', str(e.code))
        except error.URLError as e:
            print('We failed to reach a server. Reason:', str(e.reason))
        else:
            html = response.read()
            time2 = datetime.utcnow()
            print(str(num), 'got response from url', url, time2 - time1)


class WebRequestsThreaded(Thread):

    def __init__(self, urls):
        Thread.__init__(self)
        self.urls = urls
        self.wr = WebRequests()

    def run(self):
        for url in self.urls:
            self.wr.ping_website(url)


if __name__ == '__main__':
    urls = [
        ('https://www.facebook.com', 1),
        ('https://www.google.com', 2),
        ('https://www.dropbox.com', 3),
        ('https://www.airbnb.com', 4),
        ('https://www.example.com', 5),
        ('https://www.clover.com', 6),
        ('https://www.kayak.com', 7),
        ('https://www.linkedin.com', 8),
        ('https://www.tripadvisor.com', 9),
    ]
    wr = WebRequests()
    thread_count = 9
    urls_chunked = [urls[i::thread_count] for i in range(thread_count)]
    time1 = datetime.utcnow()
    threads = []
    for i in range(thread_count):
        t = WebRequestsThreaded(urls_chunked[i])
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    time2 = datetime.utcnow()
    print('Total time', time2 - time1)

__author__ = 'zhangxa'
from anger6Spider.spiders.jd_spiders import Jd_Home_Spider
from anger6Spider.env import SpiderEnv
from anger6Spider.log4s import Log4Spider
from anger6Spider.application import Application
from tornado import gen

if __name__ == "__main__":
    url_lst = ["http://www.jd.com/"]
    app = Application([
        (r"^.*$", "anger6Spider.spiders.jd_spiders.Jd_Home_Spider"),
    ])

    @gen.coroutine
    def main():
        for url in url_lst:
            fetch_one_url(url)
        yield gen.sleep(10)

    @gen.coroutine
    def fetch_one_url(url):
        env_obj = SpiderEnv(url)
        env = yield env_obj.gen_env()
        urlSeek = Jd_Home_Spider(env,app)
        yield urlSeek.work()
        for url in urlSeek.urlLists:
           Log4Spider.infoLog(url)
        Log4Spider.infoLog(len(urlSeek.urlLists))

    from tornado.ioloop import IOLoop
    IOLoop.instance().run_sync(main)


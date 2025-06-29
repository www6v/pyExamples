# https://blog.csdn.net/u012060033/article/details/140080765
'''
无栈协程 -> asyncio 
有栈协程 -> gevent 
'''

import asyncio

## case1
async def crawl_page(url):
     print('crawling {}'.format(url))
     sleep_time = int(url.split('_')[-1])
     await asyncio.sleep(sleep_time)
     print('OK {}'.format(url))


async def main(urls):
     for url in urls:
        await crawl_page(url) # 阻塞等待

def asynRun():
     asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))


## case2
async def crawl_page1(url):
     print('crawling {}'.format(url))
     sleep_time = int(url.split('_')[-1])
     await asyncio.sleep(sleep_time)
     print('OK {}'.format(url))


async def main1(urls):
     tasks = [asyncio.create_task(crawl_page1(url)) for url in urls]  ## 多任务, 异步执行
     for task in tasks:
          await task

def asynRun1():
   asyncio.run(main1(['url_1', 'url_2', 'url_3', 'url_4']))

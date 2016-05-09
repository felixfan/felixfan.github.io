---
title: scrapy simple example 抓取南京邮电大学南邮要闻
layout: post
categories: [Python]
tags: [Python]
image: /figure2016
---

{% include JB/setup %}





# 0. 安装scrapy

```
conda install scrapy # 电脑已经安装了anaconda
```

# 1. 创建一个新工程

```
scrapy startproject njupt #其中njupt是项目名称，可以按照个人喜好来定义
```

输入以上命令之后，就会看见命令行运行的目录下多了一个名为njupt的目录，目录的结构如下：

```
|---- njupt
| |---- njupt
|   |---- __init__.py
|   |---- items.py        #用来存储爬下来的数据结构（字典形式）
|    |---- pipelines.py    #用来对爬出来的item进行后续处理，如存入数据库等
|    |---- settings.py    #爬虫配置文件
|    |---- spiders        #此目录用来存放创建的新爬虫文件（爬虫主体）
|     |---- __init__.py
| |---- scrapy.cfg        #项目配置文件
```

至此，工程创建完毕。

# 2. 设置 items.py
本文以抓取南邮新闻为例，需要存储三种信息：

- 南邮新闻标题
- 南邮新闻时间
- 南邮新闻的详细链接

items.py内部代码如下：

```
# -*- coding: utf-8 -*-

import scrapy

class NjuptItem(scrapy.Item):   # NjuptItem 为自动生成的类名
    news_title = scrapy.Field() # 南邮新闻标题
    news_date = scrapy.Field()  # 南邮新闻时间
    news_url = scrapy.Field()   # 南邮新闻的详细链接
```


# 3. 编写 spider

spider是爬虫的主体，负责处理requset response 以及url等内容，处理完之后交给pipelines进行进一步处理。
设置完items之后，就在spiders目录下新建一个njuptSpider.py文件,内容如下:

```
# -*- coding: utf-8 -*-

import scrapy
from njupt.items import NjuptItem
import logging

class njuptSpider(scrapy.Spider):
    name = "njupt"
    allowed_domains = ["njupt.edu.cn"]
    start_urls = [
        "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/1/list.htm",
        ]
    
    def parse(self, response):
        news_page_num = 14
        page_num = 386
        if response.status == 200:
            for i in range(2,page_num+1):
                for j in range(1,news_page_num+1):
                    item = NjuptItem() 
                    item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                    "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                  
                    yield item
                    
                next_page_url = "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/"+str(i)+"/list.htm"
                yield scrapy.Request(next_page_url,callback=self.parse_news)
        
    def parse_news(self, response):
        news_page_num = 14
        if response.status == 200:
            for j in range(1,news_page_num+1):
                item = NjuptItem()
                item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                yield item
```

其中:

- name为爬虫名称，在后面启动爬虫的命令当中会用到。
- allowed_domains为允许爬虫爬取的域名范围（如果连接到范围以外的就不爬取）
- start_urls表明爬虫首次启动之后访问的第一个Url，其结果会被自动返回给parse函数。
- parse函数为scrapy框架中定义的内置函数，用来处理请求start_urls之后返回的response，由我们实现
- news_page_num = 14和page_num = 386分别表示每页的新闻数目，和一共有多少页，本来也可以通过xpath爬取下来的，但是我实在是对我们学校的网站制作无语了，html各种混合，于是我就偷懒手动输入了。
- 之后通过item = NjuptItem()来使用我们之前定义的item，用来存储新闻的url、标题、日期。（这里面有一个小技巧就是通过`|`来接连xpath可以一次返回多个想要抓取的xpath）
- 通过yield item来将存储下来的item交由后续的pipelines处理
- 之后通过生成next_page_url来通过scrapy.Request抓取下一页的新闻信息
- scrapy.Request的两个参数，一个是请求的URL另外一个是回调函数用于处理这个request的response，这里我们的回调函数是parse_news
- parse_news里面的步骤和parse差不多，当然你也可以改造一下parse然后直接将其当做回调函数，这样的话一个函数就ok了

# 4. 编写 pipelines.py

初次编写可以直接编辑njupt目录下的pipelines.py文件。pipelines主要用于数据的进一步处理，比如类型转换、存储入数据库、写到本地等。pipelines是在每次spider中yield item 之后调用，用于处理每一个单独的item。下面代码就是实现了在本地新建一个njupt.txt文件用于存储爬取下来的内容。

```
import sys
import json

reload(sys) 
sys.setdefaultencoding('utf-8') # 存取中文

class NjuptPipeline(object):
    def __init__(self):
        self.file = open('njupt.txt','w')
    def process_item(self, item, spider):
        self.file.write(item['news_title'])
        self.file.write("\n")
        self.file.write(item['news_date'])
        self.file.write("\n")
        self.file.write(item['news_url'])
        self.file.write("\n")
        return item
```

# 5. 编写 settings.py

settings.py文件用于存储爬虫的配置，有很多种配置，由于是入门教程，不需要配置很多，我们这里就添加一下刚才编写的pipelines就行了。文件内容如下。

```
BOT_NAME = 'njupt'

SPIDER_MODULES = ['njupt.spiders']
NEWSPIDER_MODULE = 'njupt.spiders'


ITEM_PIPELINES = {
    'njupt.pipelines.NjuptPipeline':1,
}
```

# 6. 启动爬虫与查看结果

以上步骤全部完成之后，我们就启动命令行，然后切换运行目录到njupt的spiders目录下，通过以下命令启动爬虫

```
scrapy crawl njupt
```

经过一段时间的风狂爬取，爬虫结束。

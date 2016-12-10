
from scrapy.spiders import Spider  
from scrapy.selector import Selector 
from house.items import HouseItem
import sys
import re 
reload(sys)
sys.setdefaultencoding('gb2312')  

class ZiroomSpider(Spider):
    name = "house"
    allowed_domains = ["http://bj.lianjia.com/ershoufang/"]

    sourceurl = "http://bj.lianjia.com/ershoufang/pg%s"
    #sourceurl = "http://www.ziroom.com/z/nl/z3-r2.html?p=%s"
    start_urls = [sourceurl % (x) for x in xrange(1,1066)]

    print start_urls[0]

    def parse(self, response):  
        pattern = re.compile('[\d.]+')

        sel = Selector(response)  
        # sites = sel.xpath('//ul/li')  
        items = []
        sites = sel.xpath('//div[@class="content"]//ul[@class="sellListContent"]/li')  
        for site in sites: 
            item = HouseItem()
            
            url = site.xpath('a/@href').extract() 
            thum_pic_url =  site.xpath('a/img/@data-original').extract()
            alt = site.xpath('a/img/@alt').extract()
            title = site.xpath('div[1]/div[1]/a/text()').extract()
            xiaoqu = site.xpath('div[1]/div[2]/div/a/text()').extract()
            comment = site.xpath('div[1]/div[2]/div/text()').extract()
            buildtime = site.xpath('div[1]/div[3]/div/text()').extract()
            area =  site.xpath('div[1]/div[3]/div/a/text()').extract()
            attentions = site.xpath('div[1]/div[4]/text()').extract()
            tag = site.xpath('div[1]/div[5]/span[1]/text()').extract()
            totalPrice = site.xpath('div[1]/div[6]/div[1]/span/text()').extract()
            perPrice = site.xpath('div[1]/div[6]/div[2]/span/text()').extract()

            attentionlist = attentions[0].split('/')
            commentlist = comment[2].split('|')
            # buildtimelist = buildtime.replace('-','').split(' ')
            item['url'] = title
            item['thum_pic_url'] = thum_pic_url
            item['alt'] = alt
            item['title'] = title
            item['xiaoqu'] = xiaoqu
            item['rooms'] = commentlist[1]
            item['square'] = re.findall(pattern,commentlist[2])[0]
            item['direction'] = commentlist[3]
            item['decoration'] = commentlist[4]
            # item['floorhigh'] = buildtimelist[0]
            item['buildtime'] = buildtime
            item['area'] = area
            item['follows'] = re.findall(pattern,attentionlist[0])[0] 
            item['saws'] = re.findall(pattern,attentionlist[1])[0] 
            item['tag'] = tag
            item['totalPrice'] = totalPrice
            item['perPrice'] = re.findall(pattern,perPrice[0])[0]
            items.append(item)
        return items

__author__ = 'kiruba'
import scrapy
from scrapy.spider import Spider
from scrapy.http import FormRequest
from datetime import date
from dateutil.rrule import rrule,DAILY

# 12=KARNATAKA

class MySpider(Spider):
    name = "imd_ark"
    allowed_domains = ['http://imdaws.com']
    start_urls = ["http://imdaws.com/ViewArgData.aspx"]
    state = 12
    # start_date = date(2014, 07, 04)
    # end_date = date(2014, 07, 05)
    def parse(self,response):
        yield FormRequest.from_response(response,
                                        method='POST',
                                        formname='frmDeviceData',
                                        formdata={'CmbState': "12", 'CmbDistrict':'BENGALORU RURAL',
                                                  'CmbLocation': "1716",
                                                  'txtFromDate': '04/07/2014',
                                                  'txtToDate': '10/07/2014',
                                                  'CmbTime': "",
                                                  },
                                        callback=self.parse_page
                                        )
    #  'BtnData':"View Data"}

    def parse_page(self,response):
        with open('/home/kiruba/PycharmProjects/imd_scrape/imd/test.html', 'wb') as f:
            f.write(response.body)

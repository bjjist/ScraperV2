import scrapy



class BlogSpider(scrapy.Spider):
    name = 'blogspider'
   
  
    start_urls = ['https://auto.ria.com/newauto/marka-mercedes-benz/']
    

    
    def parse(self, response):
        for car in response.css('section.proposition:nth-child(1) > a:nth-child(1)'): #< SUDA PIXAT CLASS  
            yield {'price': response.css("section.proposition > a > div > div > span:nth-child(3)").extract_first(),
                
                'name': response.css("div > div > h3 > span:nth-child(1)").extract(),
                
                'HP': response.css("div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").extract()
                }

        for next_page in response.css('span.page-item:nth-child(10) > a:nth-child(1)'):
             yield response.follow(next_page, self.parse)
       
       
           

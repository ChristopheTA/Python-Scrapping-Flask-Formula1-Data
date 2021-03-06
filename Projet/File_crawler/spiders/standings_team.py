import scrapy
from scrapy import Request
from ..items import ArticleItem

class F1Spider(scrapy.Spider):
    name = "standings_team"
    allowed_domains = ["www.formula1.com"]
    start_urls = ['https://www.formula1.com/en/results.html/2021/races.html']

    # def parse():
    #   permet de donner le lien de chaque année d'information étudiée    
    # 

    def parse(self, response):
        all_links = {
            name:response.urljoin(url) for name, url in zip(
            response.css(".resultsarchive-filter-container").css(".resultsarchive-filter-wrap")[0].css(".resultsarchive-filter-item")[1:11].css("span::text").extract(),
            response.css(".resultsarchive-filter-container").css(".resultsarchive-filter-wrap")[0].css(".resultsarchive-filter-item")[1:11].css("a::attr(href)").extract())
        }

        for link in all_links.values():
            yield Request(link, callback=self.parse_gp)
    
    # def parse_gp():
    #   permet de donner le lien de chaque résultat de Grand Prix     
    # 

    def parse_gp(self, response):
        all_links = {
            name:response.urljoin(url) for name, url in zip(
            response.css(".resultsarchive-filter-container").css(".resultsarchive-filter-wrap")[1].css(".resultsarchive-filter-item")[2].css("span::text").extract(),
            response.css(".resultsarchive-filter-container").css(".resultsarchive-filter-wrap")[1].css(".resultsarchive-filter-item")[2].css("a::attr(href)").extract())
        }
        for link in all_links.values():
            yield Request(link, callback=self.parse_standings)
    
    # def parse_standings():
    #   scrappe les informations données par les classes cherchées
    # retourne une liste d'item   
       
    def parse_standings(self, response):
        title = self.clean_spaces(response.css(".ResultsArchiveTitle").css("h1::text").extract_first())
        for article in response.css(".resultsarchive-table").css("tbody").css("tr"):
            Position = article.css(".dark")[0].css("td::text").extract_first()
            Team = article.css(".dark.bold.uppercase.ArchiveLink").css("a::text").extract_first()
            Points = article.css(".dark.bold").css("td::text").extract_first()
            yield ArticleItem(
                title = title,
                Position = Position,
                Team = Team,
                Points = Points

            )

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())


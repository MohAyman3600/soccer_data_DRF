"""Example for scraping data from Api-football-beta."""

# from scraper.model_scrapers import TeamStatsScraper
from scraper.model_scrapers import PlayerStatsScraper

url = "https://api-football-beta.p.rapidapi.com/"


headers = {
    'x-rapidapi-key': "b0b50d8d3emshbdfc9c636872541p1479bbjsn8e0b498853be",
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }
    
# s = TeamStatsScraper(url, headers)
s = PlayerStatsScraper(url, headers)

s.save_objects()
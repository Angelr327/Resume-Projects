from weather import get_weather
from sports import get_nba_games, scores, nba_report
from datetime import date , timedelta

weather_school = get_weather("Orlando,FL,USA")
weather_home = get_weather("Middletown,NY,USA")

yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

today = date.today().strftime("%Y-%m-%d")



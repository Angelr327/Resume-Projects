import requests
from datetime import date , timedelta

API_KEY = "8ec23758-2b53-4517-8190-9d474b503bdb"

yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

def get_nba_games(date):
    url = "https://api.balldontlie.io/v1/games"
    headers = {
        "Authorization": API_KEY
    }

    params = {
        "dates[]": date
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    games = data["data"]
    results = []

    for game in games:
        results.append({
            "home": game["home_team"]["full_name"],
            "away": game["visitor_team"]["full_name"],
            "home_score": game["home_team_score"],
            "visitor_score": game["visitor_team_score"],
            "status": game["status"]
        })
       
    return results

scores = get_nba_games(yesterday)

nba_report = ""

for game in scores:
    nba_report += (
        f'{game["away"]} {game["visitor_score"]} - '
        f'{game["home"]} {game["home_score"]} ({game["status"]})\n'
    )
    
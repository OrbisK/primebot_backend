import os

import requests

from app_prime_league.models import Team
from prime_league_bot import settings
from prime_league_bot.settings import BASE_URI_AJAX, BASE_URI


# api = {
#     "matches": {
#         "method": requests.get,
#         "path": {
#             settings.DEFAULT_TEAM_ID: settings.DEFAULT_GROUP_LINK,
#             "105959": "prm/1504-summer-split-2020/group/509-gruppenphase/5743-division-4-25",
#             "105878": "prm/1504-summer-split-2020/group/509-gruppenphase/5591-division-4-17",
#             "93008": "prm/1504-summer-split-2020/group/509-gruppenphase/5576-division-4-12",
#             "111914": "prm/1504-summer-split-2020/group/509-gruppenphase/5734-division-4-22",
#
#         }
#     },
#     "match_details": {
#         "method": requests.get,
#         "path": "matches/",
#     },
#     "team": {
#         "method": requests.get,
#         "path": "teams/",
#     },
# }

# api_json = {
#     "match_details": {
#         "method": requests.post,
#         "path": "leagues_match/",
#     }
# }


def get_local_response(file_path):
    with open(file_path) as file:
        website = file.read()
    return website


class Api:
    def __init__(self):
        self.base_uri = settings.BASE_URI
        self.base_uri_ajax = settings.BASE_URI_AJAX

    def json_handler(self, endpoint, request=requests.get, post_params=None):
        if endpoint is None:
            raise Exception("Endpoint not found")

        path = f"{self.base_uri}{endpoint}/"
        response = request(path, data=post_params)
        return response

    def html_handler(self, endpoint, request=requests.get, query_params=None, team_id=None):
        if endpoint is None:
            raise Exception("Endpoint not found")

        path = f"{self.base_uri}{endpoint}"
        path += "/".join(str(x) for x in [query_params]) if query_params is not None else ""
        response = request(path)
        return response


class Crawler:

    def __init__(self, local: bool = False):
        self.local = local
        self.api = Api()

    def get_matches_website(self, team: Team):
        if self.local:
            return get_local_response(
                os.path.join(os.path.dirname(settings.BASE_DIR), "static", f"matches_{team.id}.txt"))
        return self.api.html_handler(team.group_link, requests.get).text

    def get_match_website(self, match_id):
        if self.local:
            return get_local_response(
                os.path.join(os.path.dirname(settings.BASE_DIR), "static", f"match_{match_id}.txt"))
        return self.api.html_handler(f"matches/{match_id}", ).text

    def get_team_website(self, _id):
        web_site = self.api.html_handler(f"teams/{_id}").text if not self.local else get_local_response(
            os.path.join(os.path.dirname(settings.BASE_DIR), "static", f"team_{_id}.txt"))
        return web_site

    def get_details_json(self, match):
        if self.local:
            return get_local_response(
                os.path.join(os.path.dirname(settings.BASE_DIR), "static", f"match_details_json_{match}.txt"))
        return self.api.json_handler("leagues_match/", post_params={"id": match, "action": "init"}).text

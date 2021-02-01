import logging

import telepot

from app_prime_league.models import Team
from communication_interfaces.telegram_interface.tg_singleton import TelegramMessagesWrapper
from utils.utils import current_game_day


def main():
    game_day = current_game_day()

    logger = logging.getLogger("notifications_logger")
    logger.info(f"Start Sending Weekly Notifications...")
    teams = Team.objects.get_watched_team_of_current_split()
    teams = teams.filter(telegram_id__in=[-500818835, -537735976])
    for team in teams:
        if team.value_of_setting("weekly_op_link"):
            next_match = team.games_against.filter(game_day=game_day).first()
            if next_match is not None:
                logger.debug(f"Sending Weekly Notification to {team}...")
                TelegramMessagesWrapper.send_new_game_day(next_match, team.value_of_setting("pin_weekly_op_link"))


def run():
    main()

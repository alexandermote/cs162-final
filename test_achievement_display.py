#! usr/bin/env python3
# coding=utf-8

from achievement_display import api_pull, listifier, tupler, classifier
from achievement_display import Achievement
import pytest


@pytest.mark.parametrize(
    "steam_id, file",
    [
        ("", f"Please enter a valid Steam ID.\n"),
        ("0", f"Please enter a valid Steam ID.\n"),
        ("butts", f"Please enter a valid Steam ID.\n"),
        (
            "210970",
            (
                {
                    "achievementpercentages": {
                        "achievements": [
                            {"name": "endgame", "percent": 17.3999996185302734},
                            {"name": "challenge", "percent": 4},
                        ]
                    }
                }
            ),
        ),
        (
            "311690",
            (
                {
                    "achievementpercentages": {
                        "achievements": [
                            {"name": "BEAT_TUTORIAL", "percent": 91.8000030517578125},
                            {"name": "REACH_SEWERS", "percent": 40.4000015258789063},
                            {
                                "name": "PREFIRE_ON_MIMIC",
                                "percent": 34.7999992370605469,
                            },
                            {
                                "name": "SPEND_META_CURRENCY",
                                "percent": 30.1000003814697266,
                            },
                            {
                                "name": "PUSH_TABLE_INTO_PIT",
                                "percent": 28.7000007629394531,
                            },
                            {
                                "name": "UNLOCK_FLOOR_TWO_SHORTCUT",
                                "percent": 26.2000007629394531,
                            },
                            {
                                "name": "KILL_BOSS_WITH_GLITTER",
                                "percent": 25.2000007629394531,
                            },
                            {"name": "BEAT_FLOOR_ONE_MULTI", "percent": 23.5},
                            {
                                "name": "KILL_WITH_PITS_MULTI",
                                "percent": 22.2999992370605469,
                            },
                            {"name": "BEAT_FLOOR_FIVE", "percent": 21.7999992370605469},
                            {
                                "name": "BEAT_MANFREDS_RIVAL",
                                "percent": 19.7999992370605469,
                            },
                            {"name": "HAVE_MANY_COINS", "percent": 19.3999996185302734},
                            {"name": "FLIP_TABLES_MULTI", "percent": 19},
                            {
                                "name": "FALL_IN_END_TIMES",
                                "percent": 17.2999992370605469,
                            },
                            {"name": "BUILD_BULLET", "percent": 17.2000007629394531},
                            {"name": "REACH_CATHEDRAL", "percent": 16.8999996185302734},
                            {
                                "name": "COMPLETE_GUNSLING_MULTI",
                                "percent": 16.6000003814697266,
                            },
                            {
                                "name": "KILL_FROZEN_ENEMY_WITH_ROLL",
                                "percent": 15.8999996185302734,
                            },
                            {
                                "name": "BEAT_FLOOR_TWO_MULTI",
                                "percent": 15.3999996185302734,
                            },
                            {"name": "BEAT_PAST_GUIDE", "percent": 14.8000001907348633},
                            {
                                "name": "BEAT_PAST_MARINE",
                                "percent": 14.8000001907348633,
                            },
                            {"name": "BEAT_PAST_CONVICT", "percent": 14},
                            {"name": "BEAT_PAST_ROGUE", "percent": 14},
                            {"name": "UNLOCK_FLOOR_THREE_SHORTCUT", "percent": 13.5},
                            {
                                "name": "COMPLETE_GOLEM_ARM",
                                "percent": 13.1999998092651367,
                            },
                            {
                                "name": "REACH_BLACK_MARKET",
                                "percent": 12.8999996185302734,
                            },
                            {"name": "BEAT_PAST_ALL", "percent": 12.8999996185302734},
                            {"name": "BEAT_A_JAMMED_BOSS", "percent": 12.5},
                            {"name": "BEAT_FLOOR_THREE_MULTI", "percent": 12.5},
                            {"name": "HAVE_MAX_CURSE", "percent": 12},
                            {"name": "UNLOCK_ROBOT", "percent": 11.8999996185302734},
                            {"name": "MAP_MAIN_FLOORS", "percent": 11.8000001907348633},
                            {"name": "DIE_IN_PAST", "percent": 11.3000001907348633},
                            {"name": "UNLOCK_BULLET", "percent": 10.8999996185302734},
                            {
                                "name": "BEAT_FLOOR_FIVE_MULTI",
                                "percent": 10.6999998092651367,
                            },
                            {
                                "name": "BEAT_FLOOR_FOUR_MULTI",
                                "percent": 10.6000003814697266,
                            },
                            {"name": "BEAT_FLOOR_SIX", "percent": 10.1000003814697266},
                            {
                                "name": "COLLECT_FIVE_MASTERY_TOKENS",
                                "percent": 9.80000019073486328,
                            },
                            {
                                "name": "UNLOCK_FLOOR_FOUR_SHORTCUT",
                                "percent": 9.60000038146972656,
                            },
                            {"name": "POPULATE_BREACH", "percent": 8.89999961853027344},
                            {"name": "BEAT_PAST_BULLET", "percent": 8.5},
                            {
                                "name": "COMPLETE_GAME_WITH_BEAST_MODE",
                                "percent": 8.39999961853027344,
                            },
                            {"name": "BEAT_PAST_ROBOT", "percent": 8.39999961853027344},
                            {"name": "UNLOCK_FLOOR_FIVE_SHORTCUT", "percent": 8},
                            {
                                "name": "ACE_WINCHESTER_MULTI",
                                "percent": 7.80000019073486328,
                            },
                            {
                                "name": "BEAT_METAL_GEAR_RAT",
                                "percent": 6.30000019073486328,
                            },
                            {"name": "COMPLETE_GAME_WITH_ENCHANTED_GUN", "percent": 6},
                            {"name": "KILL_WITH_CHANDELIER_MULTI", "percent": 6},
                            {"name": "STEAL_MULTI", "percent": 5.69999980926513672},
                            {
                                "name": "COMPLETE_GAME_WITH_TURBO_MODE",
                                "percent": 5.40000009536743164,
                            },
                            {
                                "name": "BEAT_ADVANCED_DRAGUN",
                                "percent": 4.09999990463256836,
                            },
                            {
                                "name": "COMPLETE_GAME_WITH_CHALLENGE_MODE",
                                "percent": 3.40000009536743164,
                            },
                            {
                                "name": "COMPLETE_FRIFLE_MULTI",
                                "percent": 3.29999995231628418,
                            },
                            {
                                "name": "KILL_IN_MINE_CART_MULTI",
                                "percent": 3.09999990463256836,
                            },
                        ]
                    }
                }
            ),
        ),
    ],
)
def test_api_pull(steam_id, file):
    assert api_pull(steam_id) == file


@pytest.mark.parametrize("steam_id", ["440", "311690", "210970", "400"])
def test_listifier(steam_id):
    assert listifier(api_pull(steam_id), steam_id) == f"{steam_id}_achievements.txt"


def test_listifier_length():
    test_list = open("400_achievements.txt", "r").readlines()
    assert len(test_list) == 15


@pytest.mark.parametrize(
    "steam_id, length", [(400, 15), (440, 522), (210970, 2), (311690, 54)]
)
def test_tupler(steam_id, length):
    tuple_test_list = tupler(f"{steam_id}_achievements.txt")
    assert len(tuple_test_list) == length
    for i in tuple_test_list:
        assert len(i) == 2


def test_classifier():
    class_test_list = classifier(tupler("400_achievements.txt"))
    for i in class_test_list:
        assert isinstance(i, Achievement) == True

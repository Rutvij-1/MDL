import numpy as np
from part_2 import step_cost, MM_attack_reward, MM_dead_reward, shoot_hp, hit_hp, regain_hp


def get_actions(pos, mat, arrow, state, health):
    actions = {}
    if health == 0:
        actions["NONE"] = [
            {
                "probability": 1.0,
                "state": (pos, mat, arrow,
                          state, health),
                "reward": step_cost
            }
        ]
        return actions
    if pos == "C":
        if state == "D":
            actions["STAY"] = [
                {
                    "probability": 0.17,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["LEFT"] = [
                {
                    "probability": 0.17,
                    "state": ("W", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": ("W", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["RIGHT"] = [
                {
                    "probability": 0.2,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.8,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["UP"] = [
                {
                    "probability": 0.17,
                    "state": ("N", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": ("N", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["DOWN"] = [
                {
                    "probability": 0.17,
                    "state": ("S", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": ("S", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["SHOOT"] = [
                {
                    "probability": 0.1,
                    "state": (pos, mat, arrow-1, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.4,
                    "state": (pos, mat, arrow-1, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.1,
                    "state": (pos, mat, arrow-1, "R", max(0, health-25)),
                    "reward": step_cost
                },
                {
                    "probability": 0.4,
                    "state": (pos, mat, arrow-1, state, max(0, health-25)),
                    "reward": step_cost
                }
            ]
            if health <= shoot_hp:
                actions["SHOOT"][2]["reward"] += MM_dead_reward
                actions["SHOOT"][3]["reward"] += MM_dead_reward
            actions["HIT"] = [
                {
                    "probability": 0.18,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.72,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.02,
                    "state": (pos, mat, arrow, "R", max(0, health-50)),
                    "reward": step_cost
                },
                {
                    "probability": 0.08,
                    "state": (pos, mat, arrow, state, max(0, health-50)),
                    "reward": step_cost
                }
            ]
            if health <= hit_hp:
                actions["HIT"][2]["reward"] += MM_dead_reward
                actions["HIT"][3]["reward"] += MM_dead_reward
        else:
            actions["STAY"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["LEFT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.425,
                    "state": ("W", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["RIGHT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.5,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["UP"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.425,
                    "state": ("N", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["DOWN"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.425,
                    "state": ("S", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["SHOOT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.25,
                    "state": (pos, mat, arrow-1, state, max(0, health-25)),
                    "reward": step_cost
                },
                {
                    "probability": 0.25,
                    "state": (pos, mat, arrow-1, state, health),
                    "reward": step_cost
                }
            ]
            if health <= shoot_hp:
                actions["SHOOT"][1]["reward"] += MM_dead_reward
            actions["HIT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.05,
                    "state": (pos, mat, arrow, state, max(0, health-50)),
                    "reward": step_cost
                },
                {
                    "probability": 0.45,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            if health <= shoot_hp:
                actions["HIT"][1]["reward"] += MM_dead_reward
    if pos == "W":
        # actions += ["STAY", "RIGHT", "SHOOT"]
        if state == "D":
            actions["STAY"] = [
                {
                    "probability": 0.2,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.8,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["RIGHT"] = [
                {
                    "probability": 0.2,
                    "state": ("C", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.8,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["SHOOT"] = [
                {
                    "probability": 0.15,
                    "state": (pos, mat, arrow-1, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.6,
                    "state": (pos, mat, arrow-1, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.05,
                    "state": (pos, mat, arrow-1, "R", max(0, health-25)),
                    "reward": step_cost
                },
                {
                    "probability": 0.2,
                    "state": (pos, mat, arrow-1, state, max(0, health-25)),
                    "reward": step_cost
                }
            ]
            if health <= shoot_hp:
                actions["SHOOT"][2]["reward"] += MM_dead_reward
                actions["SHOOT"][3]["reward"] += MM_dead_reward
        else:
            actions["STAY"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.5,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["RIGHT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.5,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["SHOOT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", health+regain_hp),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.125,
                    "state": (pos, mat, arrow-1, state, max(0, health-25)),
                    "reward": step_cost
                },
                {
                    "probability": 0.375,
                    "state": (pos, mat, arrow-1, state, health),
                    "reward": step_cost
                }
            ]
            if health <= shoot_hp:
                actions["SHOOT"][1]["reward"] += MM_dead_reward
    # if pos == "E":
    #     actions += ["STAY", "LEFT", "SHOOT", "HIT"]
    # if pos == "N":
    #     actions += ["STAY", "DOWN", "CRAFT"]
    # if pos == "S":
    #     actions += ["STAY", "DOWN", "GATHER"]

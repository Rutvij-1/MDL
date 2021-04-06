import numpy as np
from part_2_config import *


def get_actions(pos, mat, arrow, state, health):
    actions = {}
    if health == 0:
        actions["NONE"] = [
            {
                "probability": 1.0,
                "state": (pos, mat, arrow, state, health),
                "reward": 0.0
            }
        ]
        return actions
    if pos == "C":
        if state == "D":
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
            if arrow > 0:
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
            actions["STAY"] = [
                {
                    "probability": 0.17,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.68,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
        else:
            actions["HIT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
            if health <= hit_hp:
                actions["HIT"][1]["reward"] += MM_dead_reward
            if arrow > 0:
                actions["SHOOT"] = [
                    {
                        "probability": 0.5,
                        "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
            actions["LEFT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
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
            actions["STAY"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
                    "reward": stay_cost + MM_attack_reward
                },
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
    if pos == "W":
        if state == "D":
            if arrow > 0:
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
            actions["STAY"] = [
                {
                    "probability": 0.2,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.8,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
        else:
            if arrow > 0:
                actions["SHOOT"] = [
                    {
                        "probability": 0.375,
                        "state": (pos, mat, arrow-1, "D", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.375,
                        "state": (pos, mat, arrow-1, state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.125,
                        "state": (pos, mat, arrow-1, "D", max(0, health-25)),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.125,
                        "state": (pos, mat, arrow-1, state, max(0, health-25)),
                        "reward": step_cost
                    }
                ]
                if health <= shoot_hp:
                    actions["SHOOT"][2]["reward"] += MM_dead_reward
                    actions["SHOOT"][3]["reward"] += MM_dead_reward
            actions["RIGHT"] = [
                {
                    "probability": 0.5,
                    "state": ("C", mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.5,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["STAY"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, arrow, "D", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.5,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
    if pos == "E":
        if state == "D":
            actions["HIT"] = [
                {
                    "probability": 0.16,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.64,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.04,
                    "state": (pos, mat, arrow, "R", max(0, health-50)),
                    "reward": step_cost
                },
                {
                    "probability": 0.16,
                    "state": (pos, mat, arrow, state, max(0, health-50)),
                    "reward": step_cost
                }
            ]
            if health <= hit_hp:
                actions["HIT"][2]["reward"] += MM_dead_reward
                actions["HIT"][3]["reward"] += MM_dead_reward
            if arrow > 0:
                actions["SHOOT"] = [
                    {
                        "probability": 0.02,
                        "state": (pos, mat, arrow-1, "R", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.08,
                        "state": (pos, mat, arrow-1, state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.18,
                        "state": (pos, mat, arrow-1, "R", max(0, health-25)),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.72,
                        "state": (pos, mat, arrow-1, state, max(0, health-25)),
                        "reward": step_cost
                    }
                ]
                if health <= shoot_hp:
                    actions["SHOOT"][2]["reward"] += MM_dead_reward
                    actions["SHOOT"][3]["reward"] += MM_dead_reward
            actions["LEFT"] = [
                {
                    "probability": 0.2,
                    "state": (E_left_dest, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.8,
                    "state": (E_left_dest, mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["STAY"] = [
                {
                    "probability": 0.2,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.8,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
        else:
            actions["HIT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.1,
                    "state": (pos, mat, arrow, state, max(0, health-50)),
                    "reward": step_cost
                },
                {
                    "probability": 0.4,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            if health <= hit_hp:
                actions["HIT"][1]["reward"] += MM_dead_reward
            if arrow > 0:
                actions["SHOOT"] = [
                    {
                        "probability": 0.5,
                        "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
                        "reward": step_cost + MM_attack_reward
                    },
                    {
                        "probability": 0.45,
                        "state": (pos, mat, arrow-1, state, max(0, health-25)),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.05,
                        "state": (pos, mat, arrow-1, state, health),
                        "reward": step_cost
                    }
                ]
                if health <= shoot_hp:
                    actions["SHOOT"][1]["reward"] += MM_dead_reward
            actions["LEFT"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
                    "reward": step_cost + MM_attack_reward
                },
                {
                    "probability": 0.5,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["STAY"] = [
                {
                    "probability": 0.5,
                    "state": (pos, mat, 0, "D", min(accepted_health[-1], health+regain_hp)),
                    "reward": stay_cost + MM_attack_reward
                },
                {
                    "probability": 0.5,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
    if pos == "N":
        if state == "D":
            if mat > 0:
                actions["CRAFT"] = [
                    {
                        "probability": 0.1,
                        "state": (pos, mat-1, min(arrow+1, accepted_arrows[-1]), "R", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.4,
                        "state": (pos, mat-1, min(arrow+1, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.07,
                        "state": (pos, mat-1, min(arrow+2, accepted_arrows[-1]), "R", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.28,
                        "state": (pos, mat-1, min(arrow+2, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.03,
                        "state": (pos, mat-1, min(arrow+3, accepted_arrows[-1]), "R", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.12,
                        "state": (pos, mat-1, min(arrow+3, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    }
                ]
            actions["DOWN"] = [
                {
                    "probability": 0.17,
                    "state": ("C", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": ("C", mat, arrow, state, health),
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
            actions["STAY"] = [
                {
                    "probability": 0.17,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.68,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
        else:
            if mat > 0:
                actions["CRAFT"] = [
                    {
                        "probability": 0.25,
                        "state": (pos, mat-1, min(arrow+1, accepted_arrows[-1]), "D", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.25,
                        "state": (pos, mat-1, min(arrow+1, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.175,
                        "state": (pos, mat-1, min(arrow+2, accepted_arrows[-1]), "D", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.175,
                        "state": (pos, mat-1, min(arrow+2, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.075,
                        "state": (pos, mat-1, min(arrow+3, accepted_arrows[-1]), "D", health),
                        "reward": step_cost
                    },
                    {
                        "probability": 0.075,
                        "state": (pos, mat-1, min(arrow+3, accepted_arrows[-1]), state, health),
                        "reward": step_cost
                    }
                ]
            actions["DOWN"] = [
                {
                    "probability": 0.425,
                    "state": ("C", mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.425,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["STAY"] = [
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, "D", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, "D", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
    if pos == "S":
        if state == "D":
            actions["UP"] = [
                {
                    "probability": 0.17,
                    "state": ("C", mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.68,
                    "state": ("C", mat, arrow, state, health),
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
            actions["GATHER"] = [
                {
                    "probability": 0.15,
                    "state": (pos, min(mat+1, accepted_materials[-1]), arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.6,
                    "state": (pos, min(mat+1, accepted_materials[-1]), arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.05,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.2,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
            ]
            actions["STAY"] = [
                {
                    "probability": 0.17,
                    "state": (pos, mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.68,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.03,
                    "state": ("E", mat, arrow, "R", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.12,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
        else:
            actions["UP"] = [
                {
                    "probability": 0.425,
                    "state": ("C", mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.425,
                    "state": ("C", mat, arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": step_cost
                }
            ]
            actions["GATHER"] = [
                {
                    "probability": 0.375,
                    "state": (pos, min(mat+1, accepted_materials[-1]), arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.375,
                    "state": (pos, min(mat+1, accepted_materials[-1]), arrow, state, health),
                    "reward": step_cost
                },
                {
                    "probability": 0.125,
                    "state": (pos, mat, arrow, "D", health),
                    "reward": step_cost
                },
                {
                    "probability": 0.125,
                    "state": (pos, mat, arrow, state, health),
                    "reward": step_cost
                },
            ]
            actions["STAY"] = [
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, "D", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.425,
                    "state": (pos, mat, arrow, state, health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, "D", health),
                    "reward": stay_cost
                },
                {
                    "probability": 0.075,
                    "state": ("E", mat, arrow, state, health),
                    "reward": stay_cost
                }
            ]
    return actions

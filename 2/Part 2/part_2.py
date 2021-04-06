import numpy as np
from action import get_actions

team_no = 7
arr = [0.5, 1.0, 2.0]
step_cost = -10.0 / arr[team_no % 3]
gamma = 0.999
delta = 0.001
MM_attack_reward = -40.0
MM_dead_reward = 50.0
shoot_hp = 25
hit_hp = 50
regain_hp = 25


accepted_positions = ["W", "N", "E", "S", "C"]
accepted_materials = [0, 1, 2]
accepted_arrows = [0, 1, 2, 3]
accepted_states = ["D", "R"]
accepted_health = [0, 25, 50, 75, 100]


actions = ["UP", "LEFT", "DOWN", "RIGHT", "STAY",
           "SHOOT", "HIT", "CRAFT", "GATHER", "NONE"]
states = []


class State:
    def __init__(self, pos, mat, arrow, state, health):
        if not pos in accepted_positions:
            raise SystemError
        if not mat in accepted_materials:
            raise SystemError
        if not arrow in accepted_arrows:
            raise SystemError
        if not state in accepted_states:
            raise SystemError
        if not health in accepted_health:
            raise SystemError
        self.pos = pos
        self.mat = mat
        self.arrow = arrow
        self.state = state
        self.health = health
        self.prev_utility = 0.0
        self.utility = 0.0

    def set_actions(self):
        self.actions = get_actions(self.pos, self.mat, self.arrow,
                                   self.state, self.health)
        for move in self.actions:
            for result in self.actions[move]:
                result["state"] = find_state(result["state"])


def generate_states():
    for pos in accepted_positions:
        for mat in accepted_materials:
            for arrow in accepted_arrows:
                for state in accepted_states:
                    for health in accepted_health:
                        states.append(State(pos, mat, arrow, state, health))


def find_state(state_tuple):
    for state in states:
        if (state_tuple[0] == state.pos and
            state_tuple[1] == state.mat and
            state_tuple[2] == state.arrow and
            state_tuple[3] == state.state and
                state_tuple[4] == state.health):
            return state
    return None


if __name__ == "__main__":
    generate_states()
    for state in states:
        state.set_actions()

    # Value Iteration Algorithm below

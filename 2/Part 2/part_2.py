import numpy as np
from part_2_action import get_actions
from part_2_config import *

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
        self.policy = None

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


def R(state, action):
    reward = 0.0
    for result in state.actions[action]:
        reward += result["probability"] * result["reward"]
    return reward


def P(state_d, state, action):
    prob = 0.0
    for result in state.actions[action]:
        if state_d == result["state"]:
            prob += result["probability"]
    return prob


def U(state, action):
    utility = R(state, action)
    for state_d in states:
        utility += state_d.prev_utility * P(state_d, state, action) * gamma
    return utility


def print_info(state, action, utility):
    print(
        f"({state.pos},{state.mat},{state.arrow},{state.state},{state.health}):{action}=["
        + "{:0.3f}]".format(round(utility, 3)))


def value_iteration(trace=True):
    n = 0
    max_diff = np.Infinity
    while max_diff >= delta:
        if trace:
            print(f"iteration={n}")
        for state in states:
            state.prev_utility = state.utility
        max_diff = 0.0
        for state in states:
            state.utility = np.NINF
            best_action = None
            highest_utility = np.NINF
            for action in state.actions:
                u = U(state, action)
                if u > highest_utility:
                    highest_utility = u
                    best_action = action
                state.utility = max(state.utility, u)
            max_diff = max(max_diff, abs(state.utility-state.prev_utility))
            state.policy = best_action
            if trace:
                print_info(state, best_action, highest_utility)
        n += 1


def random(choices, weights):
    total = 0.0
    for weight in weights:
        if weight < 0:
            raise SystemError
        total += weight
    normalized_weights = [weight / total for weight in weights]
    p = np.random.rand(1)[0]
    l = len(choices)
    for i in range(l):
        if normalized_weights[i] > p:
            return choices[i]
        p -= normalized_weights[i]
    return choices[-1]


def simulate(start_state):
    print(
        f"Start State: ({start_state.pos},{start_state.mat},{start_state.arrow},{start_state.state},{start_state.health})\n")
    curr_state = start_state
    cntr = 0
    while curr_state.health > 0:
        next_state = random(
            [result["state"]
             for result in curr_state.actions[curr_state.policy]],
            [result["probability"]
             for result in curr_state.actions[curr_state.policy]]
        )
        MM_STATUS = ""
        if curr_state.state == "D" and next_state.state == "D":
            MM_STATUS = "MM stayed in dormant state.".ljust(30)
        elif curr_state.state == "D" and next_state.state == "R":
            MM_STATUS = "MM entered in ready state.".ljust(30)
        elif curr_state.state == "R" and next_state.state == "D":
            if curr_state.pos == "C" or curr_state.pos == "E":
                MM_STATUS = "MM successfully attacked IJ.".ljust(30)
            else:
                MM_STATUS = "MM attacked IJ and failed.".ljust(30)
        else:
            MM_STATUS = "MM stayed in ready state.".ljust(30)
        curr_str = f"From state({curr_state.pos}, {curr_state.mat}, {curr_state.arrow}, {curr_state.state}, {curr_state.health}) "
        action_str = f"IJ performed the action \"{curr_state.policy}\", "
        next_str = f"and entered the state ({next_state.pos}, {next_state.mat}, {next_state.arrow}, {next_state.state}, {next_state.health}). "
        print(curr_str + action_str + next_str + MM_STATUS)
        curr_state = next_state
        cntr += 1
    print(f"\nIJ defeated MM in {cntr} time steps.")


if __name__ == "__main__":
    generate_states()
    for state in states:
        state.set_actions()

    # Trace output
    value_iteration()

    # # Simulation output
    # value_iteration(trace=False)
    # for state_tuple in start_state_tuples:
    #     print("START OF SIMULATION".center(25, "-")+"\n\n\n")
    #     simulate(find_state(state_tuple))
    #     print("\n\n\n"+"END OF SIMULATION".center(25, "-")+"\n\n\n")

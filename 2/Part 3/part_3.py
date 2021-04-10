import numpy as np
import cvxpy as cp
import os
import json
from part_3_action import get_actions
from part_3_config import *

states = []


class State:
    def __init__(self, pos, mat, arrow, state, health, idx):
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
        self.index = idx
        self.policy = None
        self.set_tuple()

    def set_tuple(self):
        self.tuple = (self.pos, self.mat, self.arrow, self.state, self.health)

    def set_actions(self):
        self.actions = get_actions(self.pos, self.mat, self.arrow,
                                   self.state, self.health)
        for move in self.actions:
            for result in self.actions[move]:
                result["state"] = find_state(result["state"])


class LP:
    def __init__(self):
        self.set_dimension()
        self.set_mat_a()
        self.set_mat_r()
        self.set_mat_alpha()
        self.set_var_x()
        self.set_policy()

    def set_dimension(self):
        self.dim = 0
        for state in states:
            self.dim += len(state.actions.keys())

    def set_mat_a(self):
        self.a = np.zeros((TOTAL_STATES, self.dim), dtype=np.float_)
        idx = 0
        for state in states:
            i = state.index
            for action, results in state.actions.items():
                if action == "NONE":
                    self.a[i][idx] += 1.0
                else:
                    for result in results:
                        self.a[i][idx] += result["probability"]
                        self.a[result["state"].index][idx] -= result["probability"]
                idx += 1

    def set_mat_r(self):
        self.r = np.zeros((1, self.dim), dtype=np.float_)
        idx = 0
        for state in states:
            for action, results in state.actions.items():
                for result in results:
                    self.r[0][idx] += result["probability"] * result["reward"]
                idx += 1

    def set_mat_alpha(self):
        self.alpha = np.zeros((TOTAL_STATES, 1), dtype=np.float_)
        self.alpha[find_state(start_state_tuple).index] = 1.0

    def set_var_x(self):
        x = cp.Variable((self.dim, 1), 'x')
        constraints = [
            cp.matmul(self.a, x) == self.alpha,
            x >= 0
        ]
        objective = cp.Maximize(cp.matmul(self.r, x))
        problem = cp.Problem(objective, constraints)
        self.objective = problem.solve()
        self.x = [float(i) for i in list(x.value)]

    def set_policy(self):
        idx = 0
        for state in states:
            state.policy = list(state.actions.keys())[np.argmax(
                self.x[idx:idx+len(state.actions.keys())])]
            idx += len(state.actions.keys())
        self.policy = [[state.tuple, state.policy] for state in states]

    def parse_output(self, dir="outputs", file="part_3_output.json"):
        self.output = {
            "a": self.a.tolist(),
            "r": [float(x) for x in np.transpose(self.r)],
            "alpha": [float(x) for x in self.alpha],
            "x": self.x,
            "policy": self.policy,
            "objective": float(self.objective)
        }
        os.makedirs(dir, exist_ok=True)
        file_name = f"./{dir}/{file}"
        with open(file_name, "w+") as f:
            f.write(json.dumps(self.output, indent=4))

        # policy_obj = {}
        # for p in self.policy:
        #     policy_obj[str(p[0])] = p[1]
        # file_name = f"./{dir}/policy_{file}"
        # with open(file_name, "w+") as f:
        #     f.write(json.dumps(policy_obj, indent=4))


def generate_states():
    for pos in accepted_positions:
        for mat in accepted_materials:
            for arrow in accepted_arrows:
                for state in accepted_states:
                    for health in accepted_health:
                        states.append(
                            State(pos, mat, arrow, state, health, len(states)))


def find_state(state_tuple):
    val = 1
    idx = accepted_health.index(state_tuple[4]) * val
    val *= len(accepted_health)
    idx += accepted_states.index(state_tuple[3]) * val
    val *= len(accepted_states)
    idx += accepted_arrows.index(state_tuple[2]) * val
    val *= len(accepted_arrows)
    idx += accepted_materials.index(state_tuple[1]) * val
    val *= len(accepted_materials)
    idx += accepted_positions.index(state_tuple[0]) * val
    return states[idx]


if __name__ == "__main__":
    generate_states()
    for state in states:
        state.set_actions()

    lp = LP()
    lp.parse_output()

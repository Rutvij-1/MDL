import numpy as np

team_no = 7
arr = [0.5, 1.0, 2.0]
step_cost = -10.0 / arr[team_no % 3]
gamma = 0.999
delta = 0.001

accepted_positions = ["W", "N", "E", "S", "C"]
accepted_materials = [0, 1, 2]
accepted_arrows = [0, 1, 2, 3]
accepted_states = ["D", "R"]
accepted_health = [0, 25, 50, 75, 100]


actions = ["UP", "LEFT", "DOWN", "RIGHT", "STAY",
           "SHOOT", "HIT", "CRAFT", "GATHER", "NONE"]


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
        self.utility = 0.0
        self.set_actions()

    def set_actions(self):
        self.actions = []
        if self.health == 0:
            self.actions += ["NONE"]
            return
        if self.pos == "C":
            self.actions += ["STAY", "LEFT", "RIGHT",
                             "UP", "DOWN", "SHOOT", "HIT"]
        if self.pos == "W":
            self.actions += ["STAY", "RIGHT", "SHOOT"]
        if self.pos == "E":
            self.actions += ["STAY", "LEFT", "SHOOT", "HIT"]
        if self.pos == "N":
            self.actions += ["STAY", "DOWN", "CRAFT"]
        if self.pos == "S":
            self.actions += ["STAY", "DOWN", "GATHER"]

team_no = 7
arr = [0.5, 1.0, 2.0]
step_cost = -10.0 / arr[team_no % 3]

gamma = 0.999  # Task 1
# gamma = 0.25  # Task 2 Case 3
delta = 0.001

MM_attack_reward = -40.0
MM_dead_reward = 50.0
stay_cost = step_cost  # Task 1
# stay_cost = 0.0  # Task 2 Case 2

shoot_hp = 25
hit_hp = 50
regain_hp = 25

accepted_positions = ["W", "N", "E", "S", "C"]
accepted_materials = [0, 1, 2]
accepted_arrows = [0, 1, 2, 3]
accepted_states = ["D", "R"]
accepted_health = [0, 25, 50, 75, 100]
accepted_actions = ["UP", "LEFT", "DOWN", "RIGHT", "STAY",
                    "SHOOT", "HIT", "CRAFT", "GATHER", "NONE"]

start_state_tuples = [("W", 0, 0, "D", 100), ("C", 2, 0, "R", 100)]

E_left_dest = "C"  # Task 1
# E_left_dest = "W"  # Task 2 Case 1

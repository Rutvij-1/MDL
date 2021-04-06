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

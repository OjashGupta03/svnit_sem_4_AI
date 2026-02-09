import random


ADJ = {
    "A": {"RIGHT": "B", "LEFT": "A"},
    "B": {"RIGHT": "C", "LEFT": "A"},
    "C": {"RIGHT": "C", "LEFT": "B"},
}

status_to_id = {"clean": 0, "dirty": 1}
id_to_status = {0: "clean", 1: "dirty"}


RULES = {
    ("A", 1): "SUCK",
    ("A", 0): "RIGHT",
    ("B", 1): "SUCK",
    ("B", 0): "RANDOM_MOVE",
    ("C", 1): "SUCK",
    ("C", 0): "LEFT",
}


ACTION_COST = {"SUCK": 2, "LEFT": 1, "RIGHT": 1}
DIRT_PENALTY = 10


class VacuumAgent:
    def __init__(self, environment, start="A"):
        self.env = environment
        self.loc = start
        self.total_cost = 0

    def perceive(self):
        return (self.loc, status_to_id[self.env[self.loc]])

    def decide(self, percept):
        action = RULES[percept]
        if action == "RANDOM_MOVE":
            action = random.choice(["LEFT", "RIGHT"])
        return action

    def act(self, action):
        if action == "SUCK":
            self.env[self.loc] = "clean"
        else:
            self.loc = ADJ[self.loc][action]

    def random_dirty(self, p=0.4):
        for r in self.env:
            if self.env[r] == "clean" and random.random() < p:
                self.env[r] = "dirty"

    def step_cost(self, action):
        dirty_rooms = sum(1 for r in self.env if self.env[r] == "dirty")
        return dirty_rooms * DIRT_PENALTY + ACTION_COST[action]

    def run(self, steps=15, seed=1, p_dirty=0.1):
        random.seed(seed)

        print(
            "step | percept          | action | loc | A     B     C     | step_cost | total_cost"
        )
        print(
            "-----|------------------|--------|-----|-------------------|-----------|-----------"
        )

        for step in range(1, steps + 1):
            percept = self.perceive()
            action = self.decide(percept)
            self.act(action)

            # environment change
            self.random_dirty(p_dirty)

            cost = self.step_cost(action)
            self.total_cost += cost

            loc, sid = percept
            print(
                f"{step:>4} | ({loc},{id_to_status[sid]:<5})        | {action:<6} | "
                f"{self.loc:^3} | {self.env['A']:<5} {self.env['B']:<5} {self.env['C']:<5} | "
                f"{cost:>9} | {self.total_cost:>10}"
            )


# ----- main -----
if __name__ == "__main__":
    env = {"A": "dirty", "B": "dirty", "C": "dirty"}
    agent = VacuumAgent(env, start="B")
    agent.run(steps=20, seed=2, p_dirty=0.12)

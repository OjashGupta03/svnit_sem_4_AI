class LevelCrossingAgent:
    def rule(self, train, obstacle, emergency):


        if emergency == "Active":
            return ("Lower Gate", "Siren ON", "RED") if train == "Detected" else ("Lower Gate", "Siren OFF", "RED")


        if train == "Detected" and obstacle == "Blocked":
            return ("Lower Gate", "Siren ON", "RED") if emergency == "Active" else ("Raise Gate", "Siren ON", "RED")

        if train == "Detected" and obstacle == "Clear":
            return ("Lower Gate", "Siren ON", "GREEN")
            
        if train == "Not Detected":
            return ("Raise Gate", "Siren OFF", "RED")

percepts = [
    ("Not Detected", "Clear", "Neutral"),
    ("Detected", "Clear", "Neutral"),
    ("Detected", "Clear", "Active"),
    ("Detected", "Blocked", "Neutral"),
    ("Detected", "Clear", "Active")
]


agent = LevelCrossingAgent()


print("Percept (Train, Obstacle, Emergency) -> Action")
print("\n")

for p in percepts:



    action = agent.rule(*p)
    print(f"{p} -> {action}")
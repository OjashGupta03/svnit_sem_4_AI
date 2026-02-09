enviroment={track sensors,obstacle,emergency,
    gates,hooters}
rules={
    if "EMERGENCY_STOP" in enviroment->stop train immediately
}
class LevelCrossingEnvironment:
    def __init__(self):
        self.track_sensors = [0,0]
        self.obstacle = None
        self.emergency = False
        self.gates = []
    def perceive(self):
        return {
            "track_sensors": self.track_sensors,
            "obstacle": self.obstacle,
            "emergency": self.emergency,
        }
    def rules(self,percept):
        if self.emergency:
            return "EMERGENCY_STOP"
        if self.obstacle is not None:
            return "STOP_TRAIN"
        if self.track_sensors[0] or self.track_sensors[1]:
            return "CLOSE_GATES"
        if self.track_sensors == [0, 0]:
            return "OPEN_GATES"
        return "NO_ACTION"
    
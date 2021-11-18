from arrow import StraightArrow, CurvedArrow
from traffic_light_controller import State, TrafficLightController


class States:
    S1 = State("1")
    S2 = State("2")
    S3 = State("3")
    S4 = State("4")
    S5 = State("5")
    S6 = State("6")

    RED = 0
    YELLOW = 1
    GREEN = 2


class TSectionTrafficLightController(TrafficLightController):
    def __init__(self):
        defaultDur = 1
        durations = {
            States.S1: defaultDur,
            States.S2: defaultDur,
            States.S3: defaultDur,
            States.S4: defaultDur,
            States.S5: defaultDur,
            States.S6: defaultDur,
        }
        super().__init__(durations)

        self.arrows = self.initArrows()

    @staticmethod
    def __redStateMap():
        return {
            States.S1: States.RED,
            States.S2: States.RED,
            States.S3: States.RED,
            States.S4: States.RED,
            States.S5: States.RED,
            States.S6: States.RED,
        }

    def initArrows(self):
        arrows = []

        stateMap = self.__redStateMap()
        stateMap[States.S1] = States.GREEN
        stateMap[States.S2] = States.GREEN
        stateMap[States.S3] = States.GREEN
        stateMap[States.S4] = States.YELLOW
        arrow = StraightArrow(90, 90, stateMap)
        arrows.append(arrow)

        stateMap = self.__redStateMap()
        stateMap[States.S1] = States.GREEN
        stateMap[States.S2] = States.YELLOW
        arrow = StraightArrow(350, 130, stateMap)
        arrow.rotate(180)
        arrows.append(arrow)

        stateMap = self.__redStateMap()
        stateMap[States.S5] = States.GREEN
        stateMap[States.S6] = States.YELLOW
        arrow = StraightArrow(290, 190, stateMap)
        arrow.rotate(90)
        arrows.append(arrow)

        stateMap = self.__redStateMap()
        stateMap[States.S3] = States.GREEN
        stateMap[States.S4] = States.YELLOW
        arrow = CurvedArrow(180, 140, stateMap)
        arrows.append(arrow)

        return arrows

    def updateDurations(self, t1: int, t2: int, t3: int, *, tYellowLight: int = 2):
        self.stateDurations[States.S1] = t1
        self.stateDurations[States.S2] = tYellowLight
        self.stateDurations[States.S3] = t2
        self.stateDurations[States.S4] = tYellowLight
        self.stateDurations[States.S5] = t3
        self.stateDurations[States.S6] = tYellowLight

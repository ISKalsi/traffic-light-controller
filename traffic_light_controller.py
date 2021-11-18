import pygame


class State:
    __total = 0

    def __init__(self, name: str):
        self.__name = name
        self.__index = State.__total
        State.__total += 1

    @property
    def name(self):
        return self.__name

    @property
    def index(self):
        return self.__index

    def __eq__(self, other):
        if issubclass(type(other), State):
            return self.__name == other.name
        else:
            return self is other

    def __hash__(self):
        return self.__name.__hash__()

    def __repr__(self):
        return "State(%s)" % self.name

    def __del__(self):
        State.__total -= 1


class TrafficLightController:
    def __init__(self, stateDurations: dict[State, int]):
        self.states: list[State] = [key for key in stateDurations.keys()]
        self.currentState = self.states[0]
        self.stateDurations = stateDurations
        self.transitionTable = self.__generateTransitionTable()
        self.timeline: list[State] = []
        self.arrows = []

    def __generateTransitionTable(self) -> dict[State, State]:
        transitionTable = {}
        noOfStates = len(self.states)
        for i in range(noOfStates):
            transitionTable[self.states[i]] = self.states[(i + 1) % noOfStates]
        return transitionTable

    def addArrowsToGroup(self, group: pygame.sprite.Group):
        for arrow in self.arrows:
            group.add(arrow)

    def updateArrowStates(self, t: int):
        for arrow in self.arrows:
            arrow.changeState(self.timeline[t - 1])

    def runFor(self, duration: int):
        self.timeline.clear()
        globalTime = 1
        stateTime = 1
        while globalTime <= duration:
            self.timeline.append(self.currentState)
            if stateTime < self.stateDurations[self.currentState]:
                stateTime += 1
            else:
                stateTime = 1
                self.currentState = self.transitionTable[self.currentState]
            globalTime += 1

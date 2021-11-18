import PySimpleGUI as sg
import pygame_gui as gui
import pygame_gui.elements as guiElements
from pygame.rect import Rect

from values import Values

size = Values.WINDOW_SIZE
width = size[0]
height = size[1]
margin = 10


class UI:
    def __init__(self):
        self.manager = gui.UIManager(Values.WINDOW_SIZE)

        self.controlPanel = ControlPanel(self.manager)
        self.statePanel = StatePanel(self.manager)
        self.timerPanel = TimerPanel(self.manager)

        self.enterDurationsDialog = EnterDurationsDialogBox()


class ControlPanel:
    def __init__(self, uiManager):
        buttonWidth = 100
        buttonHeight = 50

        rect = Rect(0, 0, buttonWidth, buttonHeight)
        rect.bottomleft = width - 220, height - 20 - margin
        self.backward = guiElements.UIButton(
            text="backward",
            object_id="backward",
            relative_rect=rect,
            manager=uiManager,
        )
        self.backward.hide()

        rect = Rect(0, 0, buttonWidth, buttonHeight)
        rect.bottomleft = width - 120, height - 20 - margin
        self.forward = guiElements.UIButton(
            text="forward",
            object_id="forward",
            relative_rect=rect,
            manager=uiManager,
        )
        self.forward.hide()

        rect = Rect(0, 0, buttonWidth, buttonHeight)
        rect.bottomleft = width - 160, height - 80 - margin
        self.durations = guiElements.UIButton(
            text="durations",
            object_id="durations",
            relative_rect=rect,
            manager=uiManager,
        )

    def showControls(self):
        self.forward.show()
        self.backward.show()


class TimerPanel:
    def __init__(self, uiManager):
        rect = Rect(0, 0, 40, 40)
        rect.topright = width - margin, margin
        self.globalTimer = guiElements.UILabel(
            text="1",
            object_id="timeLabel",
            relative_rect=rect,
            manager=uiManager,
        )

    def updateGlobalTimer(self, t: int):
        self.globalTimer.set_text("%s" % t)


class StatePanel:
    def __init__(self, uiManager):
        self.currentTime = "0"

        rect = Rect(0, 0, 250, 100)
        rect.bottomleft = margin, height - margin
        self.state = guiElements.UILabel(
            text="Current state: 0",
            object_id="wordLabel",
            relative_rect=rect,
            manager=uiManager,
        )

    def setState(self, newState: str):
        self.state.set_text("Current state: %s" % newState)


class EnterDurationsDialogBox:
    def __init__(self):
        self.t1 = "0"
        self.t2 = "0"
        self.t3 = "0"

    def show(self):
        layout = [
            [sg.Text("Please enter durations for all states:")],
            [sg.Column(
                [[sg.InputText(key='-T1-', size=(3, 1)),
                  sg.InputText(key='-T2-', size=(3, 1)),
                  sg.InputText(key='-T3-', size=(3, 1))]],
                justification='center'
            )],
            [sg.Column([[
                sg.Button("OK", font="any 14", bind_return_key=True),
                sg.Exit(font="any 14")]],
                justification='right'
            )]
        ]
        window = sg.Window('', layout, font="any 17", no_titlebar=True)

        while True:
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                print("game exit. ByeBye!")
                window.close()
                return
            elif event == 'OK':
                self.t1 = values['-T1-']
                self.t2 = values['-T2-']
                self.t3 = values['-T3-']
                if self.t1 != "" and self.t2 != "" and self.t3:
                    window.close()
                    return

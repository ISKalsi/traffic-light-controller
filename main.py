import pygame
import pygame_gui

from t_section_traffic_light_controller import TSectionTrafficLightController
from ui import UI
from values import Values

pygame.init()

size = Values.WINDOW_SIZE
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Traffic Light Controller")
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

ui = UI()

tlc = TSectionTrafficLightController()
tlc.addArrowsToGroup(sprites)

tSectionImg = pygame.image.load("assets/t-section-road.jpg").convert()
tSectionImg = pygame.transform.scale(tSectionImg, Values.WINDOW_SIZE)

time = 1


def update(delta):
    screen.blit(tSectionImg, ((0, 0), Values.WINDOW_SIZE))
    sprites.draw(screen)
    ui.manager.update(delta)
    ui.manager.draw_ui(screen)
    pygame.display.flip()


def updateState():
    global time
    ui.timerPanel.updateGlobalTimer(time)
    ui.statePanel.setState(tlc.timeline[time - 1].name)
    tlc.updateArrowStates(time)
    sprites.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ui.controlPanel.backward:
                    if time-1 >= 1:
                        time -= 1
                        updateState()
                elif event.ui_element == ui.controlPanel.forward:
                    if time+1 <= len(tlc.timeline):
                        time += 1
                        updateState()
                elif event.ui_element == ui.controlPanel.durations:
                    ui.enterDurationsDialog.show()
                    tlc.updateDurations(
                        int(ui.enterDurationsDialog.t1),
                        int(ui.enterDurationsDialog.t2),
                        int(ui.enterDurationsDialog.t3)
                    )
                    tlc.runFor(30)
                    ui.controlPanel.showControls()
                    updateState()

        ui.manager.process_events(event)

    dt = clock.tick(60) / 1000
    update(dt)

pygame.quit()

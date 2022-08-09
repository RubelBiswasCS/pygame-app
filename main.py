import pygame, sys

mousedown_pos = None
mouseup_pos = None
mousedown_x_pos = None
mouseup_x_pos = None
mode_list = []
def draw_icon():
    # icon_rect = icon_surface.get_rect(center=(x_pos, 160))
    # info_icon_rect = info_icon_surface.get_rect(center=(x_pos+display_width, 160))
    # access_icon_rect = access_icon_surface.get_rect(center=(x_pos+display_width+display_width, 160))
    # screen.blit(icon_surface, icon_rect)
    # screen.blit(info_icon_surface, info_icon_rect)
    # screen.blit(access_icon_surface, access_icon_rect)
    for idx, mode in enumerate(mode_list):
        mode_rect = mode.get_rect(center=(x_pos+(display_width*idx), 160))
        screen.blit(mode, mode_rect)


pygame.init()

display_width = 320
display_height = 320
fps = 30

icon_width = 320
icon_height = 320



screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/bg_image.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (display_width, display_height))
icon_surface = pygame.image.load('assets/talk.png').convert_alpha()
icon_surface = pygame.transform.scale(icon_surface, (icon_width, icon_height))

info_icon_surface = pygame.transform.scale(
                        pygame.image.load('assets/info.png').convert_alpha(), (icon_width, icon_height))
access_icon_surface = pygame.transform.scale(
                        pygame.image.load('assets/access.png').convert_alpha(), (icon_width, icon_height))

mode_list = [icon_surface, info_icon_surface, access_icon_surface]
x_pos = display_width/2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown_pos = pygame.mouse.get_pos()
            mousedown_x_pos = x_pos
            # print(mousedown_pos)
            # print('mousebtn down', x_pos)
        if event.type == pygame.MOUSEBUTTONUP:
            mouseup_pos = pygame.mouse.get_pos()
            mouseup_x_pos = x_pos
            # print(mouseup_pos)
            # print('mousebtn up', x_pos)
    screen.blit(bg_surface, (0,0))

    if mousedown_pos:
        current_mouse_pos = pygame.mouse.get_pos()
        x_pos = mousedown_x_pos-(mousedown_pos[1]-current_mouse_pos[0])

    if(mousedown_pos and mouseup_pos):
        if mousedown_pos[0] > mouseup_pos[0]:
            x_pos = mousedown_x_pos-320
            mouseup_x_pos = None
            mousedown_pos = None
            mouseup_pos = None
        elif mousedown_pos[0] < mouseup_pos[0]:
            x_pos = mousedown_x_pos+320
            mousedown_x_pos = None
            mousedown_pos = None
            mouseup_pos = None

    draw_icon()
    # print(x_pos)
    if x_pos <= (-480*2)+190:
        x_pos = 160
    elif x_pos >= 160+190:
        x_pos = (-480)

    pygame.display.update()
    clock.tick(fps)
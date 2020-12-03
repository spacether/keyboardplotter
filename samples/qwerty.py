import keyboardlayout as kl
import pygame

def get_keyboard(layout_name: str) -> kl.KeyboardLayout:
    key_size = 60
    grey = pygame.Color('grey')
    keyboard_info = kl.KeyboardInfo(
        position=(0, 0),
        padding=2,
        color=~grey
    )
    key_info = kl.KeyInfo(
        size=(key_size, key_size),  # width, height
        margin=10,
        color=grey,
        txt_color=~grey,  # invert grey
        txt_font=pygame.font.SysFont('Arial', key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
    keyboard_layout = kl.KeyboardLayout(
        layout_name,
        keyboard_info,
        key_info
    )
    return keyboard_layout

def run_until_user_closes_window():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False

    pygame.quit()

def keyboard_example(layout_name: str):
    pygame.init()
    keyboard = get_keyboard(layout_name)

    screen = pygame.display.set_mode(
        (keyboard.rect.width, keyboard.rect.height))
    screen.fill(pygame.Color('black'))

    keyboard.draw(screen)
    pygame.display.update()
    run_until_user_closes_window()

if __name__ == "__main__":
    keyboard_example('qwerty')
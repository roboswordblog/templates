import pygame

def text(window, text, x, y, font_size, color, font_name="assets/font.otf", antialias=True):
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(str(text), antialias, color)
    window.blit(text_surface, (x, y))

shopScroll = 0
SHOP_PANEL_WIDTH = 325
CARD_HEIGHT = 95
CARD_SPACING = 10
class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        color,
        hover_color,
        border_color,
        text_color,
        function,
        args=(),
        border_width=4,
        font_size=30
    ):
        self.rect = pygame.Rect(x, y, width, height)

        self.text = text

        self.color = color
        self.hover_color = hover_color
        self.border_color = border_color
        self.text_color = text_color

        self.function = function
        self.args = args

        self.border_width = border_width
        self.font_size = font_size

        self.clicked = False
        self.pressed = False


    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()

        hover = self.rect.collidepoint(mouse_pos)

        if hover:
            fill = self.hover_color
        else:
            fill = self.color


        # fake pixel shadow
        shadow_rect = self.rect.copy()
        shadow_rect.x += 6
        shadow_rect.y += 6

        pygame.draw.rect(
            window,
            (20,20,20),
            shadow_rect
        )


        # main button
        pygame.draw.rect(
            window,
            fill,
            self.rect
        )


        # pixel border
        pygame.draw.rect(
            window,
            self.border_color,
            self.rect,
            self.border_width
        )


        # top highlight
        highlight = pygame.Rect(
            self.rect.x + 5,
            self.rect.y + 5,
            self.rect.width - 10,
            8
        )

        pygame.draw.rect(
            window,
            tuple(min(c+70,255) for c in fill),
            highlight
        )


        # bottom dark edge
        bottom = pygame.Rect(
            self.rect.x + 5,
            self.rect.bottom - 12,
            self.rect.width - 10,
            7
        )

        pygame.draw.rect(
            window,
            tuple(max(c-70,0) for c in fill),
            bottom
        )


        # text
        font = pygame.font.Font(
            "assets/font.otf",
            self.font_size
        )

        txt = font.render(
            self.text,
            False,   # important for pixel fonts
            self.text_color
        )


        txt_rect = txt.get_rect(
            center=self.rect.center
        )


        # tiny pixel shadow behind text
        shadow = font.render(
            self.text,
            False,
            (0,0,0)
        )

        window.blit(
            shadow,
            (txt_rect.x+3, txt_rect.y+3)
        )

        window.blit(
            txt,
            txt_rect
        )


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]


        if self.rect.collidepoint(mouse_pos):

            if mouse_pressed and not self.clicked:
                self.clicked = True

                self.function(*self.args)


        if not mouse_pressed:
            self.clicked = False
class NormalButton:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        function,
        args=(),
        color=(80,80,80),
        hover_color=(110,110,110),
        pressed_color=(50,50,50),
        border_color=None,
        border_width=0,
        text=None,
        text_color=(255,255,255),
        font_size=20
    ):
        self.rect = pygame.Rect(x, y, width, height)

        self.function = function
        self.args = args

        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color

        self.border_color = border_color
        self.border_width = border_width

        self.text = text
        self.text_color = text_color
        self.font_size = font_size

        self.clicked = False

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        hover = self.rect.collidepoint(mouse_pos)

        if hover and mouse_down:
            color = self.pressed_color
        elif hover:
            color = self.hover_color
        else:
            color = self.color

        radius = 12

        # Shadow
        shadow = self.rect.move(4, 4)
        pygame.draw.rect(
            window,
            (25, 25, 25),
            shadow,
            border_radius=radius
        )

        # Main button
        pygame.draw.rect(
            window,
            color,
            self.rect,
            border_radius=radius
        )

        # Border
        if self.border_color:
            pygame.draw.rect(
                window,
                self.border_color,
                self.rect,
                width=self.border_width,
                border_radius=radius
            )

        # Top shine
        highlight = pygame.Rect(
            self.rect.x + 4,
            self.rect.y + 4,
            self.rect.width - 8,
            8
        )

        pygame.draw.rect(
            window,
            tuple(min(c + 35, 255) for c in color),
            highlight,
            border_radius=6
        )

        # Text
        if self.text:
            font = pygame.font.Font(
                "assets/font.otf",
                self.font_size
            )

            shadow = font.render(
                self.text,
                True,
                (0, 0, 0)
            )

            text = font.render(
                self.text,
                True,
                self.text_color
            )

            rect = text.get_rect(center=self.rect.center)

            window.blit(shadow, (rect.x + 2, rect.y + 2))
            window.blit(text, rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]


        if self.rect.collidepoint(mouse_pos):

            if mouse_pressed and not self.clicked:
                self.clicked = True

                self.function(*self.args)


        if not mouse_pressed:
            self.clicked = False

sayingButton = NormalButton(
    x=620,
    y=485,
    width=150,
    height=55,
    function=lambda: None,
    color=(70, 70, 70),
    hover_color=(100, 100, 100),
    pressed_color=(50, 50, 50),
    border_color=(255, 255, 255),
    border_width=2,
    text="Next",
    text_color=(255, 255, 255),
    font_size=22
)

def addSayingBoxes(window, message, buttonText, function):
    global sayingButton

    # Update the existing button
    sayingButton.text = buttonText
    sayingButton.function = function

    # Dialogue box
    box = pygame.Surface((800, 170), pygame.SRCALPHA)
    box.fill((0, 0, 0, 180))
    window.blit(box, (0, 430))

    # Border
    pygame.draw.rect(window, (255, 255, 255), (0, 430, 800, 170), 3)

    # Wrapped text
    font = pygame.font.Font("assets/font.otf", 22)

    words = message.split()
    line = ""
    y = 450

    for word in words:
        test = line + word + " "
        if font.size(test)[0] < 570:
            line = test
        else:
            window.blit(font.render(line, True, (255, 255, 255)), (20, y))
            y += 30
            line = word + " "

    if line:
        window.blit(font.render(line, True, (255, 255, 255)), (20, y))

    sayingButton.draw(window)
    sayingButton.update()

buyButton = NormalButton(
    x=0,
    y=0,
    width=120,
    height=45,
    function=lambda: None,
    color=(70, 170, 70),
    hover_color=(95, 205, 95),
    pressed_color=(45, 130, 45),
    border_color=(255, 255, 255),
    border_width=2,
    text="BUY",
    text_color=(255, 255, 255),
    font_size=22
)
buyButtons = {}

def drawShopCard(window, ability, x, y, cost, function, money):
    global buyButtons

    if ability not in buyButtons:
        buyButtons[ability] = NormalButton(
            x=x + 30,
            y=y + 100,
            width=120,
            height=45,
            function=function,
            color=(50, 180, 70),
            hover_color=(70, 220, 90),
            pressed_color=(35, 140, 55),
            border_color=(255, 255, 255),
            border_width=2,
            text="BUY",
            text_color=(255,255,255),
            font_size=20
        )

    button = buyButtons[ability]

    button.rect.x = x + 30
    button.rect.y = y + 100
    button.function = function

    pygame.draw.rect(window, (45,45,55), (x,y,180,170), border_radius=12)
    pygame.draw.rect(window, (170,170,170), (x,y,180,170), 2, border_radius=12)

    text(window, ability, x + 15, y + 30, 20, (255,255,255))
    text(window, f"${cost}", x + 15, y + 60, 20, (255,215,0))

    if money >= cost:
        button.color = (50,180,70)
        button.hover_color = (70,220,90)
        button.pressed_color = (35,140,55)

        button.draw(window)
        button.update()
    else:
        button.color = (90,90,90)
        button.hover_color = (90,90,90)
        button.pressed_color = (90,90,90)

        button.draw(window)

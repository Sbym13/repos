import pygetwindow as gw
import pyautogui
from PIL import Image, ImageDraw
import time

class GameWindow:
    def __init__(self, title):
        self.window = gw.getWindowsWithTitle(title)[0]
        self.x, self.y = self.window.left, self.window.top
        self.width, self.height = self.window.width, self.window.height

    def get_screenshot(self):
        return pyautogui.screenshot()

    def draw_rectangle(self, image):
        draw = ImageDraw.Draw(image)
        draw.rectangle([self.x + 12, self.y + 28, self.x + 12 + self.width - 55, self.y + 28 + self.height - 40], outline="red")
        return image

    def draw_minimap_rectangle(self, image):
        minimap_x, minimap_y = self.get_minimap_coordinates()
        draw = ImageDraw.Draw(image)
        draw.rectangle([minimap_x, minimap_y, minimap_x + 170, minimap_y + 165], outline="blue")
        return image

    def get_minimap_coordinates(self):
        minimap_x = self.x + self.width - 213
        minimap_y = self.y + 28
        return minimap_x, minimap_y

# Criar uma instância da classe GameWindow para a janela do jogo "RuneLite"
game_window = GameWindow("RuneLite")
time.sleep(2)

# Obter uma captura de tela e desenhar um retângulo em volta da área da janela do jogo
screenshot = game_window.get_screenshot()
screenshot_with_rectangle = game_window.draw_rectangle(screenshot)

# Desenhar um retângulo na área onde fica o minimapa
screenshot_with_minimap_rectangle = game_window.draw_minimap_rectangle(screenshot_with_rectangle)

# Salvar a captura de tela com os retângulos desenhados
screenshot_with_minimap_rectangle.save("captura_com_retangulos.png")

# Imprimir as coordenadas do minimapa
minimap_x, minimap_y = game_window.get_minimap_coordinates()
print(f"Coordenadas do minimapa: x={minimap_x}, y={minimap_y}")
print(f"Coordenadas janela: x={game_window.x}, y={game_window.y}, width={game_window.width}, height={game_window.height}")
print(f"Coordenadas jogo: x={game_window.x + 12}, y={game_window.y + 28}, width={game_window.width - 55}, height={game_window.height - 40}")

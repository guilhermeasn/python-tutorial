import pyautogui
import time

# Pausa entre cada comando
pyautogui.PAUSE = .5

# Abrir o MSEdge
pyautogui.hotkey('win', 'r')
pyautogui.write('msedge')
pyautogui.press('enter')

# Acessar github
pyautogui.write('https://github.com/guilhermeasn')
pyautogui.press('enter')
time.sleep(5)

# Maximiza a janela
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('win', 'down')
pyautogui.hotkey('win', 'up')

# Pinned repositories
time.sleep(10)
pyautogui.moveTo(x=662, y=271)
pyautogui.scroll(-600)

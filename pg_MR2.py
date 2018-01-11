import pyautogui as pg
import time

pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.3)
pg.hotkey('winleft','up')
pg.typewrite('amazon.com\n',0.3)
time.sleep(4)
pg.click(265, 172,1)
pg.typewrite('fuzzy hat\n', 0.2)
pg.moveTo(1356, 130, 3)
pg.dragTo(1356, 194, 5)
pg.moveTo(617, 432, 3)
pg.click(617, 432, 1)
time.sleep(4)
pg.moveTo(1217, 547,3)
pg.click(1217, 547,1)                 


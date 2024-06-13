import win32gui
import pyautogui
import time

# 要打开的软件窗口的标题
window_title = "Banana"

# 将最小化的窗口恢复到界面上
def restore_window():
    window = win32gui.FindWindow(None, window_title)
    win32gui.ShowWindow(window, 9)  # 9表示恢复窗口
    win32gui.SetForegroundWindow(window)

def click():
    # 获取屏幕的宽度和高度
    screen_width, screen_height = pyautogui.size()

    # 计算屏幕中心的位置
    center_x, center_y = screen_width / 2, screen_height / 2

    # 移动光标到屏幕中心并点击
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()

def close_window():
    window = win32gui.FindWindow(None, window_title)
    win32gui.ShowWindow(window, 6)  # 6表示最小化窗口
    
# 主函数
while True:
    restore_window()
    time.sleep(1)#等待1秒
    click()# 调用click函数进行点击
    close_window()
    time.sleep(10860)#等待3小时1分钟



import pyautogui as pya
import time
import keyboard
import threading
from rich.console import Console
from rich.live import Live

console = Console()

sellbutton = [728, 834]
itemframe = [1051, 306]
runs = 0
running = True

console.print("[cyan]Starting in 5 seconds...")
console.print("[cyan]Pos cursor on sold itemframe!")
time.sleep(5)
buyframe = pya.position()
console.print("[green]Script started!")


def key_listener():
    global running
    keyboard.wait('esc') 
    console.print("[red]Script stopped.")
    running = False

listener_thread = threading.Thread(target=key_listener)
listener_thread.start()
with Live(console=console) as live:
    while running:
        pya.moveTo(sellbutton)
        pya.click()
        pya.moveTo(itemframe)
        pya.click()
        pya.click()
        pya.moveTo(buyframe)
        pya.click()
        pya.click()
        runs += 1
        updated_text = "[bright_magenta]Press [ESC] to stop the script!\n              runs: {}[/]".format(runs)
        live.update("\r[bright_magenta]=========================================\n{}\n=========================================".format(updated_text))
        time.sleep(0.1)

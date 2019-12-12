from win10toast import ToastNotifier as toast
import time
def display():
    time.sleep(1200)
    n = toast()
    #download any suitable icon of your choice and rename it icon.ico
    n.show_toast("WARNING","It has been 20 mins since you last took a break, now look 20ft. away for 20seconds :)",icon='icon.ico',duration=12)
    display()

if __name__ == '__main__':
    display()

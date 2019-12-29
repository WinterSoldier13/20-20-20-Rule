'''PYTHON 2 Script'''

import notify2
import time

notify2.init('')


def display():
    time.sleep(1200)
    n = notify2.Notification("Alert",
                         "It has been 20 mins since you last took a break, now look 20ft. away for 20seconds :)",
                         "icon.ico"   # Icon name
                        )
    n.show()
    #download any suitable icon of your choice and rename it icon.ico
    display()

if __name__ == '__main__':
    display()
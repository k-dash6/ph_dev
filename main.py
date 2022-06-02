from apps import *

PROJ_ROOT = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

if __name__ == '__main__':
    eel.init(f"{PROJ_ROOT}/web")
    eel.start("web_main.html", size=(1200, 800))

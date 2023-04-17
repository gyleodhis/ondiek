import shutil
import os

from src.utils.config import ondiek_main_dir

home_dir = os.path.expanduser('~')
ondiek_dir = ondiek_main_dir
ondiek_path = os.path.join(home_dir, ondiek_dir)
app_name = 'MyFirstApp'
base_dir = './src'

def create_main_dir():
    isExist = os.path.exists(ondiek_path)
    try:
        if isExist:
            return print("Directory '%s' already exists" % ondiek_path)
        elif not isExist:
            os.makedirs(ondiek_path,exist_ok = False)
            return print("Directory '%s' created successfuly" % ondiek_path)
    except OSError as error:
        return print("Directory '%s' can not be created" % ondiek_path)
# create_main_dir()

def create_base_app(app = app_name):
    create_main_dir()
    global app_path
    app_path = os.path.join(ondiek_path, app)
    isExist = os.path.exists(app_path)
    try:
        if isExist:
            print("Application: '%s' already exists" % app)
        elif not isExist:
            shutil.copytree(base_dir, app_path)
            print("Application: '%s' created successfuly" % app)
            print("App location: '%s'" % app_path)
    except OSError as error:
        print("Directory '%s' can not be created" % app_path)
create_base_app()

def launcher():
    os.chdir(app_path)
    import index.py as main
    return main
launcher()
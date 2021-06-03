from app import create_app
from flask_script import Manager,Server 


#creating app instance
app=create_app('development')


manager= manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run() # method to launch our server


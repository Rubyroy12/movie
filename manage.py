from app import create_app,db
from flask_script import Manager,Server 
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Role,Review



#creating app instance
# app=create_app('development')
app=create_app('production')
# app=create_app('tests')

manager= Manager(app)
manager.add_command('server',Server)  
#Initailaize Migrate   

migrate= Migrate(app,db)
manager.add_command('db',MigrateCommand)

#use shell decorator to make shell context
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User= User,Role=Role)




if __name__ == '__main__':
    manager.run() # method to launch our server


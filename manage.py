from app.models import User
from app import create_app,db
from flask_script import Manager, Server
from  flask_migrate import  Migrate,MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView







app = create_app('production')
manager = Manager(app)
manager.add_command('server', Server)
migrate =Migrate(app,db)
manager.add_command('db', MigrateCommand)

admin = Admin(app,name='Control Panel',)

admin.add_view(ModelView(User,db.session))


@manager.shell
def make_shell_context():
    return dict(app = app,db=db,User=User)
if __name__ == '__main__':
    manager.run()
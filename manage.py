#!/usr/bin/env python
# -*- coding: UTF-8 -*
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Option, Command, Server

from app import create_app, db
from app.main.models import eShopPrice

app = create_app(os.getenv('ESHOPPRICES_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, eShopPrice=eShopPrice)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

manager.add_command("runserver", Server(host="0.0.0.0", port=(os.environ.get('PORT') or 8000)))



@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()


def init_app_data():
    db.drop_all()
    db.create_all()

    db.session.commit()
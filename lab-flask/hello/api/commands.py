import click
from api.models import db, User

def setup_commands(app):
    @app.cli.command("insert-test-users")
    @click.argument("count")
    def insert_test_users(count):
        print("creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@gmail.com"
            user.password = "1qazxsw2"
            user.is_active = True
            
            db.session.add(user)
            db.session.commit()
            print("user:", user.email, " created.")

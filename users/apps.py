from django.apps import AppConfig
import users


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.models

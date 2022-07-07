from django.apps import AppConfig


#class HomeConfig(AppConfig):
   # name = 'Home'

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home'

    def ready(self):
        import Home.signals
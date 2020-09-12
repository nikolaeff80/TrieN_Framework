import views
from mainlib.fwsgi import Application

urlpatterns = {
    '/': views.IndexView(),
    '/index/': views.IndexView(),
    '/about/': views.AboutView(),
    '/contacts/': views.ContactsView(),
}


def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)
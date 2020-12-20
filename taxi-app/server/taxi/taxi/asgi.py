"""
ASGI config for taxi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from taxi.middleware import TokenAuthMiddlewareStack
import trips.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	"websocket": TokenAuthMiddlewareStack(
		URLRouter(
			trips.routing.websocket_urlpatterns
		)
	),
})

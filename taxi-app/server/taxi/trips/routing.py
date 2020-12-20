from django.urls import path
# from channels.routing import ProtocolTypeRouter, URLRouter


from trips.consumers import TaxiConsumer


websocket_urlpatterns = [
	path('taxi/', TaxiConsumer.as_asgi()),
]

# application = ProtocolTypeRouter({
# 	'websocket': TokenAuthMiddlewareStack(
# 		URLRouter([
# 			path('taxi/', TaxiConsumer),
# 		])
# 	),
# })
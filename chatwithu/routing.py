from channels.routing import ProtocolTypeRouter
from django.core.exceptions import AppRegistryNotReady

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
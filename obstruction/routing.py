from channels.routing import URLRouter
from channels.routing import ProtocolTypeRouter
application = ProtocolTypeRouter({
    # (your routes here)
})
# routes defined for channel calls
# this is similar to the Django urls, but specifically for Channels

URLRouter([])
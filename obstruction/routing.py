from channels.routing import URLRouter

# routes defined for channel calls
# this is similar to the Django urls, but specifically for Channels

URLRouter([
    #re_path(r"^longpoll/$", LongPollConsumer.as_asgi()),
    #re_path(r"^notifications/(?P<stream>\w+)/$", LongPollConsumer.as_asgi()),
    #re_path(r"", get_asgi_application()),
])
# from django.contrib.messages import context_processors
from django.contrib.messages.api import get_messages
from django.contrib.messages.constants import DEFAULT_LEVELS

class MessagesCustomMiddleware(object):

    def process_request(self, request):
        if not hasattr(request, 'context'):
            request.context = {}
        request.context.update({
            'messages': get_messages(request),
            'DEFAULT_MESSAGE_LEVELS': DEFAULT_LEVELS,
            })

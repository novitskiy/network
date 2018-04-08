from .forms import SubscriberForm


def handle_subscriber_form(request):
    subscriber_form = SubscriberForm()
    return locals()

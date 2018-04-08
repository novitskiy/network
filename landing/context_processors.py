from .forms import SubscriberForm


def get_subscriber_form(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return locals()

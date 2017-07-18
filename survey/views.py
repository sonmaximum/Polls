from django.views.generic import CreateView, DetailView

# Create your views here.
from survey.models import Response, Poll


class NewResponse(CreateView):
    model = Response
    fields = ("question", "answer")

    def get_success_url(self):
        #TODO: Reverse Me
        return "/survey/1/"

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save()
        return super(NewResponse, self).form_valid(form)


class PollResults(DetailView):
    model = Poll


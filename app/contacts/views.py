from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact
from .forms import *
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db import transaction

def index(request):
    context = {
        "contacts":Contact.objects.all()
    }
    return render(request, 'index.html', context)

def contact_details(request, pk):
    context = {
        "contact":Contact.objects.get(pk=pk)
    }
    return render(request, 'contact_details.html', context)



class ContactNumberCreate(CreateView):
    model = Contact
    fields = ['name',]
    # success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ContactNumberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['contact_numbers'] = NumberFormSet(self.request.POST)
        else:
            data['contact_numbers'] = NumberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        numbers = context['contact_numbers']
        with transaction.atomic():
            self.object = form.save()

            if numbers.is_valid():
                numbers.instance = self.object
                numbers.save()
        return super(ContactNumberCreate, self).form_valid(form)

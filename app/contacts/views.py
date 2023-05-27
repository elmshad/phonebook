
from django.forms import formset_factory
from .forms import ContactForm, NumberForm
from .forms import ContactForm, NumberFormSet
from django.shortcuts import render, redirect
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


def add_contact(request):
    contact_form = ContactForm(request.POST or None)
    NumberFormSet = formset_factory(NumberForm, extra=1)
    number_formset = NumberFormSet(request.POST or None, prefix='number')

    if request.method == 'POST':
        if contact_form.is_valid() and number_formset.is_valid():
            # Save the contact
            contact = contact_form.save()

            # Save associated numbers
            for form in number_formset:
                if form.is_valid():
                    number = form.save(commit=False)
                    number.contact = contact
                    number.save()

            # Redirect or do further processing

    context = {
        'contact_form': contact_form,
        'number_formset': number_formset,
    }

    return render(request, 'contacts/add_contact.html', context)





class ContactNumberCreate(CreateView):
    model = Contact
    fields = ['name',]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
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
        return super().form_valid(form)

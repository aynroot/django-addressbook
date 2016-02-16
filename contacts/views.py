from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email']


def list_contacts(request, template_name='contacts_list.html'):
    contacts = Contact.objects.order_by('first_name')
    return render(request, template_name, {'contacts': contacts})


def create_new_contact(request, template_name='edit_contact.html'):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_contacts')
    return render(request, template_name, {'form': form})


def edit_contact(request, pk, template_name='edit_contact.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('list_contacts')
    return render(request, template_name, {'form': form})


def delete_contact(request, pk, template_name='confirm_delete_contact.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('list_contacts')
    return render(request, template_name, {'contact': contact})


def contact_details(request, pk, template_name='contact_details.html'):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, template_name, {'contact': contact})

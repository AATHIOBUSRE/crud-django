from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import ContactDetails

# View to list all contacts
def contact_list(request):
    context = {'contact_list': ContactDetails.objects.all()}
    return render(request, "contact_details/contact_list.html", context)

# View to handle both insert and update of contact
def contact_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContactForm()
        else:
            contact = get_object_or_404(ContactDetails, pk=id)
            form = ContactForm(instance=contact)
        return render(request, "contact_details/contact_form.html", {'form': form})
    
    else:  # POST request
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contact = get_object_or_404(ContactDetails, pk=id)
            form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('/contacts/list/')  # Redirect only on valid form
        else:
            # If validation fails (e.g., invalid email), return form with errors
            return render(request, "contact_details/contact_form.html", {'form': form})

# View to delete a contact by ID
def contact_delete(request, id):
    contact = get_object_or_404(ContactDetails, pk=id)
    contact.delete()
    return redirect('/contacts/list/')

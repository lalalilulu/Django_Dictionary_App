from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .models import Dictionary
from .forms import InputForm
from .forms import AddForm
from django.contrib import messages
from .utils import fill_model
from django.conf import settings
import os

def home(request):
    # TODO: replace with second migration
    # fill_model(os.path.join(settings.BASE_DIR,"dict_page","data.json"))
    form = InputForm()
    return render(request, 'home.html', {'form' : form})

def get_query(request):
    form = InputForm(request.GET)
    if form.is_valid():
        word = form.cleaned_data['word']
        dictionary = Dictionary.objects.filter(word=word).first()
        if dictionary is None:
            messages.error(request, _('A word was not found in the dictionary'))
            return render(request, 'home.html', {'form' : form})
        context = {'form' : form, 'definition' : dictionary.definition}
        return render(request, 'home.html', context)
    messages.error(request, 'Your input has error')
    return render(request, 'home.html', {'form' : form})

def about(request):
    context = {}
    return render(request, "about.html", context)

def content(request):
    all_words = Dictionary.objects.all
    if request.method == 'POST':
        form = AddForm(request.POST)
        if not form.is_valid():
            messages.success(request, 'You should add a word and a definition!')
            return render(request, 'content.html', {'form': form, 'all_words': all_words})

        form.save()
        messages.success(request, 'A new word has been added to the dictionary')
    return render(request, 'content.html', {'form': AddForm(), 'all_words': all_words})



def delete(request, dictionary_id):
	w = Dictionary.objects.get(pk=dictionary_id)
	w.delete()
	messages.success(request, 'Word Has Been Deleted!')
	return redirect('content')


# def translate(request, w):
#     w = w.lower()
#     if w in data:
#         return data[w]
#     elif w.title() in data:
#         return data[w.title()]
#     elif w.upper() in data:
#         return data[w.upper()]
#     elif len(get_close_matches(w, data.keys())) > 0:
#         y = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
#         if y == "Y":
#             return data[get_close_matches(w, data.keys())[0]]
#         elif y == "N":
#             return "The word doesn't exist. Please double check it."
#         else:
#             return "Your entry isn't understood."
#     else:
#         return "The word doesn't exist. Please double check it."

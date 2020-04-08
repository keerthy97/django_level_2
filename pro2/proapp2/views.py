from django.shortcuts import render
# from django.http import HttpResponse
from proapp2.models import User
from proapp2.forms import NewUserForm


# Create your views here.
def index_1(request):
    return render(request, 'proapp2/index_1.html')


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index_1(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'proapp2/users.html', {'form': form})

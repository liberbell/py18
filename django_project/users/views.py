from django.shortcuts import render

# Create your views here.
def register(request):
    from = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
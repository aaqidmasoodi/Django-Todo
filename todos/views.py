from django.shortcuts import render
from todos.forms import TodoForm
from todos.models import Todo

def home_view(request):

    todos = Todo.objects.all() # fetches all the todos form the database


    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid(): # all clean funcitons are run
            form.save()

    else:
        form = TodoForm()
  

    context = {
        "todos": todos,
        "pizza": form
    }


    return render(request, 'index.html', context)
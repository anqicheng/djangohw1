from django.shortcuts import render

# Create your views here.
# from homepage.models import blog

def home(request):
    # all_objects=blog.objects.all()

    # first_object = all_objects[0]
    template="home.html"
    context = {
        # "variable1":all_objects,
        # "variable2": first_object,
        # "thisisavariable": title_first_object,
    }
    return render(request, template, context)
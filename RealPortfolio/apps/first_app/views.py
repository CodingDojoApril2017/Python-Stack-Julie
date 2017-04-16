from django.shortcuts import render

#@app.route  ("/")
def index(request):
    return render(request, "first_app/index.html")

#@app.route ("/")
def show(request):
    print(request.method)
    return render(request, "first_app/about.html")

def projects(request):
    print(request.method)
    return render(request, "first_app/projects.html")

def testimonials(request):
    print(request.method)
    return render(request, "first_app/testimonials.html")

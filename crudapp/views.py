from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Emp_Data_Table
from django.db.models import Q
# Create your views here.


def homePage(request):
    # this is used to select all data from database
    # select *from (table_name);
    data = Emp_Data_Table.objects.all()
    return render(request, 'index.html', {"data": data})


def addPage(request):
    # this is used to insert data into database
    if request.method == "POST":
        data = Emp_Data_Table(
            firstname=request.POST.get("firstname"),
            lastname=request.POST.get("lastname"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            dsg=request.POST.get("dsg"),
            salary=request.POST.get("salary"),
            city=request.POST.get("city"),
            state=request.POST.get("state"))
        data.save()
        return HttpResponseRedirect("/")
    return render(request, 'add_record.html')


def deletePage(request, id):
    # this query write for delete an id from database
    # get() method is used find only specific values from database
    try:
        em = Emp_Data_Table.objects.get(id=id)
        if (em):
            em.delete()
            return HttpResponseRedirect('/')
    except:
        pass
    return HttpResponseRedirect("/")


def updatePage(request, id):
    # this orm create for updating data into databasea
    data = Emp_Data_Table.objects.get(id=id)
    if (data):
        if (request.method == "POST"):
            data.firstname = request.POST.get("firstname")
            data.lastname = request.POST.get("lastname")
            data.email = request.POST.get("email")
            data.phone = request.POST.get("phone")
            data.dsg = request.POST.get("dsg")
            data.salary = request.POST.get("salary")
            data.city = request.POST.get("city")
            data.state = request.POST.get("state")
            data.save()
            return HttpResponseRedirect('/')
        return render(request, "update.html", {'data': data})
    return HttpResponseRedirect('/')


def errorPage(request):
    return render(request, 'not_found.html')


def searchPage(request):
    if (request.method == 'POST'):
        search = request.POST.get('search')
        data = Emp_Data_Table.objects.filter(Q(firstname__contains=search)|Q(lastname__contains=search))
        return render(request, 'index.html', {'data': data})
    else:
        # Redirect to a different URL, for example, the home page
        return redirect('/')  # Use redirect instead of HttpResponseRedirect

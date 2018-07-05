from django.shortcuts import render, redirect
from todolist.models import Todo


# Create your views here.
def home(request):
    if request.method == "POST":
        if request.POST.get("event") == "":
            lst = Todo.objects.all()
            return render(request, 'home.html', {"err": "请输入内容", "lst": lst})
        else:
            events = Todo(events=request.POST.get("event"), finished=False)
            events.save()
            lst = Todo.objects.all()
            return render(request, 'home.html', {"info": "添加成功", "lst": lst})
    else:
        lst = Todo.objects.all()
        return render(request, 'home.html', {"lst": lst})


def about(request):
    return render(request, 'about.html')


def cross(request, v_id):
    if request.POST.get("status") == "1":
        event = Todo.objects.get(id=v_id)
        event.finished = True
        event.save()
    else:
        event = Todo.objects.get(id=v_id)
        event.finished = False
        event.save()
    return redirect('home')


def edit(request, v_id):
    if request.method == "POST":
        if request.POST.get("changedevent") == "":
            return render(request, 'edit.html', {"err": "请输入内容"})
        else:
            event = Todo.objects.get(id=v_id)
            event.events = request.POST.get("changedevent")
            event.save()
            return redirect('home')
    else:
        event = Todo.objects.get(id=v_id)
        return render(request, 'edit.html', {"event": event})


def dele(request, v_id):
    event = Todo.objects.get(id=v_id)
    event.delete()
    return redirect('home')

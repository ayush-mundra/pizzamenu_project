from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from django.contrib.auth.models import User

def _pizzatype(request):
	if(request.method=="POST"):
		if(request.POST["_pizzatype"] and request.POST["_pizzasize"] and request.POST["_pizzatopping"]):
			_pizza=Pizza()
			_pizza.pizza_type=request.POST["_pizzatype"]
			_pizza.pizza_size=request.POST["_pizzasize"]
			_pizza.pizza_topping=request.POST["_pizzatopping"]
			_pizza.owner=request.user
			_pizza.save()

			return render(request, "index2.html")

		return render(request, "index1.html", {"error":"fill all the inputs"})

	return render(request, "index1.html")

def showall(request):
    pizza = Pizza.objects
    return render(request,'index3.html',{'pizza':pizza})

def filter(request):
	if(request.method=="POST"):
		if(request.POST["_pizzasize"] and request.POST["_pizzatopping"]):
			pizzasize=request.POST["_pizzasize"]
			pizzatopping=request.POST["_pizzatopping"]
			piz = Pizza.objects
			return render(request,'index4.html',{'piz':piz,"pizzasize":pizzasize, "pizzatopping":pizzatopping })

		return render(request, "index6.html", {"error":"fill all the inputs"})

	return render(request, "index6.html")
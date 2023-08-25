from doctest import OutputChecker
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .templatetags.forms import GreetingForm
from .templatetags.models import Item
from .templatetags.my_script import bubble_sort, calculate_result
from .templatetags.utils import calculate, calculate_total
import logging


def calculator(request):
    import requests
    if request.method == 'POST':
        operation = request.POST.get('operation')
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        
        result = calculate(operation, num1, num2)
        context = {
            'operation': operation,
            'num1': num1,
            'num2': num2,
            'result': result
        }
        return render(request, 'calculator.html', context)
    else:
        return render(request, 'calculator.html')


def quantity(request):  
    import requests
    if request.method == 'POST':
        price = float(request.POST.get('price'))
        quantity = float(request.POST.get('quantity'))

        total = calculate_total(price, quantity)
        rounded = round(total, 2)
        context = {
            'price': price,
            'quantity': quantity,
            'total': total,
            'rounded': rounded
        }
        return render(request, 'quantity.html', context)
    else:
        return render(request, 'quantity.html')


def process_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # Get the input from the form
        # Perform any processing you need on user_input
        request.session['user_input'] = 'user_name'
        logging.info(user_input)
        return render(request, 'enter.html', {'user_input': user_input})
    
def display_items(request):
    if request.method == 'POST':
        item = request.POST.get('item', '')
        description = request.POST.get('description', '')
        return render(request, 'enter.html', {'item': item, 'description': description})
    
def display_items(request):
    items = Item.objects.all()
    return render(request, 'enter.html', {'items': items})


def greet_with_form(request):
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            myname = form.cleaned_data['myname']
            request.session['myname'] = 'setname'
            setname = request.session.get('myname', '')
            myaddress = form.cleaned_data['address']
            age = form.cleaned_data['age'] + 2
            logging.info(myname)
        return render(request, 'enter.html', {'myname': myname, 'setname': setname})
    else:
        form = GreetingForm()
    return render(request, 'enter.html', {'form': form})


def base_return(request):
    import json
    import requests
    myname = request.POST.get('myname', '')

    return render(request, 'base.html', {'myname': myname})


def enter(request):
    import json
    import requests
    user_input = request.POST.get('user_input', '') 
    form = GreetingForm(request.POST or None)
    items = request.POST.get('item', '') + request.POST.get('description', '')
    description = request.POST.get('description', '')
    item = request.POST.get('item', '')
    myname = request.POST.get('myname', '')
    age = request.POST.get('age', '')
    logging.info(myname)

   
    def get_form_name(request):
        form_name = request.session.get('myname', None)
        return render(request, 'enter.html', {'form_name': form_name})
        

    
    return render(request, 'enter.html', {
        'user_input': user_input,
        'items': items,
        'description': description,
        'item': item,
        'form': form,
        'myname': myname,
        'age': age,
       })



def airviews(request):
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37201&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
        
    try: 
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error.."
    

    if api[1]['Category']['Name'] == "Good":
        category_description = "Air quality is considered satisfactory, and air pollution poses little or no risk."  
        category_color = "good" 
    elif api[1]['Category']['Name'] == "Moderate":
        category_description = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."  
        category_color = "moderate"     
    elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        category_description = "Although general public is not likely to be affected at this air quality range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."  
        category_color = "usg"     
    elif api[1]['Category']['Name'] == "Unhealthy":
        category_description = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."  
        category_color = "unhealthy"     
    elif api[1]['Category']['Name'] == "Very Unhealthy":
        category_description = "Health alert: Everyone may experience more serious health effects."  
        category_color = "veryunhealthy"     
    elif api[1]['Category']['Name'] == "Hazardous":
        category_description = "Health warnings of emergency conditions.  The entire population is more likely to be affected."  
        category_color = "hazardous"  


    return render(request, 'airviews.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color,
        })





def airhtml(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        output = calculate_result()
        result = bubble_sort()
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
    
        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."
        

        return render(request, 'airhtml.html', {'api': api, 'zipcode': zipcode, 'bubble_sort': bubble_sort, 'output': output, 'result': result})
    
    else:  
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37201&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
        output = calculate_result()
        result = bubble_sort()

        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."


        return render(request, 'airhtml.html', {'api': api, 'result': result, 'output': output})

def display_session(request):
    myname = request.session.get('myname', None)
    return render(request, 'enter.html', 'airhtml.html', 'airviews.html', 'calculator.html', 'quantity.html', {'myname': myname})

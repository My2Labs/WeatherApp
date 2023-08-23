from doctest import OutputChecker
from unittest import result
from django.shortcuts import render

from .templatetags.forms import GreetingForm
from .templatetags.models import Item
from .templatetags.my_script import bubble_sort, calculate_result


def enter(request):
    import json
    import requests
    user_input = request.POST.get('user_input', '') 
    form = GreetingForm(request.POST or None)
    items = request.POST.get('item', '') + request.POST.get('description', '')
    description = request.POST.get('description', '')
    item = request.POST.get('item', '')
        
    
    def process_input(request):
        if request.method == 'POST':
            user_input = request.POST.get('user_input', '')  # Get the input from the form
            # Perform any processing you need on user_input

            return render(request, 'enter.html', {'user_input': user_input})
    
    def greetings(request):
        name = "Alice"
        
    def greet_with_form(request):
        form = GreetingForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            return render(request, 'enter.html', {'name': name, 'address': address, 'form': form})
        return render(request, 'enter.html', {'form': form})
        
    # def display_items(request):
    #     items = Item.objects.all()
    #     return render(request, 'enter.html', {'items': items})

    def display_items(request):
        if request.method == 'POST':
            item = request.POST.get('item', '')
            description = request.POST.get('description', '')
            return render(request, 'enter.html', {'item': item, 'description': description})

    return render(request, 'enter.html', {
        'user_input': user_input,
        'items': items,
        'description': description,
        'item': item,
        'form': form,
        
        })



def about(request):
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


    return render(request, 'about.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color,
        })





def index(request):
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
        

        return render(request, 'index.html', {'api': api, 'zipcode': zipcode, 'bubble_sort': bubble_sort, 'output': output, 'result': result})
    
    else:  
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37201&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
        output = calculate_result()
        result = bubble_sort()

        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."


        return render(request, 'index.html', {'api': api, 'result': result, 'output': output})
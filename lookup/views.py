from django.shortcuts import render


def index(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
        
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


        return render(request, 'index.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color})

        return render(request, 'index.html', {
            'zipcode': zipcode})


    else:  
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


        return render(request, 'index.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color})



def about(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37201&distance=25&API_KEY=60CCA6E7-534C-4471-A04F-0DAA8BADD8A7")
    
    try: 
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error.."
    
    return render(request, 'about.html', {'api': api,})
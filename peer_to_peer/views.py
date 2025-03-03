from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.conf import settings
from django.http import JsonResponse
from .forms import UserProfileForm, RiderProfileForm, RiderTripForm,UserTripForm,CreateRideForm,CreateUserForm
from .models import UserProfile, RiderProfile, RiderTrip,UserTrip,CreateRide,CreateUser
from web3 import Web3
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def login_user(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             users=UserProfile.objects.all()
#             # for user in users:
#             #     print(user.username)
#             latest_user = UserProfile.objects.latest('id')
#             print(f"Last user added: Username - {latest_user.username}, Password - {latest_user.password}")
#             return redirect('preference')  # Replace 'home' with your desired redirect URL after login
#     else:
#         form = UserProfileForm()
#     return render(request,'login_user.html',{'form': form})

def login_rider(request):
    if request.method == 'POST':
        form = RiderProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            # Check if the username exists in the CreateRide model
            user_exists =  user_exists = CreateRide.objects.filter(Username=username).exists()

            if user_exists:
                form.save()
                latest_user = RiderProfile.objects.latest('id')
                print(f"Last user added: Username - {latest_user.username}, Password - {latest_user.password}")
                return redirect('rider_path')  # Redirect to the rider path or another page
            else:
                form.add_error('username', 'This username does not have an associated account. Please create an account first.')
    else:
        form = RiderProfileForm()

    return render(request, 'login_rider.html', {'form': form})

 

def login_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Check if the username exists in either UserProfile or CreateUser
            user_exists = UserProfile.objects.filter(username=username).exists() or CreateUser.objects.filter(Username=username).exists()

            if user_exists:
                # Authenticate the user (assuming a standard authentication process)
                user_profile = UserProfile.objects.filter(username=username).first()

                if user_profile :
                #and user_profile.password == password:
                    # If the username and password are correct, save the form data
                    form.save()
                    latest_user = UserProfile.objects.latest('id')
                    print(f"Last user added: Username - {latest_user.username}, Password - {latest_user.password}")
                    return redirect('preference')  # Redirect to preference or another page
                else:
                    # Handle invalid password case
                    form.add_error('password', 'Invalid password.')
            else:
                # Handle case where the username doesn't exist
                form.add_error('username', 'This username does not have an associated account. Please create an account first.')
    else:
        form = UserProfileForm()

    return render(request, 'login_user.html', {'form': form})




'''def create_account(request):
    if request.method == 'POST':
        # Add account creation logic here
        pass
    return render(request, 'create_account.html')'''

def two_verify(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        
        # Process the verification code, e.g., check if it is correct
        if verification_code == "123456":  # Example check
            return render("Verification successful!")
        else:
            return render("Invalid verification code.")

    return redirect('login_user')

'''def create_rider_acc(request):
    if request.method == 'POST':
        # Add account creation logic here
        pass
    return render(request, 'create_rider_acc.html')  '''


def rider_path(request):
    if request.method == 'POST':
        form = RiderTripForm(request.POST)
        if form.is_valid():
            form.save()
            paths = RiderTrip.objects.all()
            # for path in paths:
            #     print(path.source)
            #     print(path.destination)
            latest_path = RiderTrip.objects.latest('id')
            print(f"Last path added: Source - {latest_path.source}, Destination - {latest_path.destination}")
            return redirect('map_leaflet')  # Replace 'some_next_page' with your desired redirect URL after form submission
    else:
        form = RiderTripForm()
    return render(request, 'rider_path.html', {'form': form})

def user_path(request):
    if request.method == 'POST':
        form = UserTripForm(request.POST)
        if form.is_valid():
            form.save()
            paths = UserTrip.objects.all()
            # for path in paths:
            #     print(path.source)
            #     print(path.destination)
            latest_path = UserTrip.objects.latest('id')
            print(f"Last path added: Source - {latest_path.source}, Destination - {latest_path.destination}")
            return redirect('map_user')  # Replace 'some_next_page' with your desired redirect URL after form submission
    else:
        form = UserTripForm()
    return render(request, 'user_path.html', {'form': form})
       

def create_rider_acc(request):
    if request.method == 'POST':
        print("hi")
        form = CreateRideForm(request.POST)
        if form.is_valid():
            form.save()
            print("hello")
            # Optionally, you might want to print or log details
            rides = CreateRide.objects.all()
            # for ride in rides:
            #     print(ride.vehicle_no)
            latest_ride = CreateRide.objects.latest('id')
            print(f"Last ride added: Name - {latest_ride.Name},Email - {latest_ride.email},Age - {latest_ride.age},Phone_no - {latest_ride.phone_no},vehicle_Type - {latest_ride.vehicle_type},Vehicle_no - {latest_ride.vehicle_no}, Aadhaar.no - {latest_ride.aadhaar_no}, License_no - {latest_ride.license_no}")
            return redirect('login_rider')  # Replace 'home' with your desired redirect URL after form submission
        else:
            print(form.errors)
    else:
        form = CreateRideForm()
    return render(request, 'create_rider_acc.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("hello")
            # Optionally, you might want to print or log details
            users = CreateUser.objects.all()
            # for user in users:
            #     print("HELLO")
            #     print(user.Username)
            #     print(user.email)
            latest_user = CreateUser.objects.latest('id')
            print(f"Last user added: Name - {latest_user.Name}, Email - {latest_user.email},Phone.no - {latest_user.phone_no},Priority.no - {latest_user.priority_no},Age - {latest_user.age},Username - {latest_user.Username},Password - {latest_user.password}")
            return redirect('login_user')  # Replace 'home' with your desired redirect URL after form submission
    else:
        form = CreateUserForm()
    return render(request, 'create_account.html', {'form': form})


    #return render(request, 'map_leaflet.html')

def map_leaflet(request):
    return render(request, 'map_leaflet.html')
    # if request.method == 'POST':
    #     form = mapRiderForm(request.POST)
    #     if form.is_valid():
    #         # Save the form data and store addresses in session
    #         ride = form.save()
    #         request.session['source_address'] = ride.source
    #         request.session['destination_address'] = ride.destination
    #         return redirect('map_leaflet')

    # else:
    #     form = mapRiderForm()

    # # Retrieve addresses from session
    # source_address = request.session.get('source_address', '')
    # destination_address = request.session.get('destination_address', '')

    # return render(request, 'map_leaflet.html', {
    #     'form': form,
    #     'source_address': source_address,
    #     'destination_address': destination_address
    # })


def map_user(request):
    return render(request, 'map_user.html')
    # if request.method == 'POST':
    #     form = mapRiderForm(request.POST)
    #     if form.is_valid():
    #         # Save the form data
    #         ride = form.save()

    #         # Get the source and destination from the form
    #         source_address = ride.source
    #         destination_address = ride.destination

    #         # Print the source and destination to the terminal (for debugging)
    #         print(f"Source Address: {source_address}")
    #         print(f"Destination Address: {destination_address}")

    #         # Fetch the latitude and longitude for both addresses using a geocoding API
    #         def get_lat_lon(address):
    #             response = requests.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json&addressdetails=1")
    #             data = response.json()
    #             if data:
    #                 return data[0]['lat'], data[0]['lon']
    #             return None, None

    #         source_lat, source_lon = get_lat_lon(source_address)
    #         destination_lat, destination_lon = get_lat_lon(destination_address)

    #         # Calculate the distance between the source and destination
    #         def calculate_distance(lat1, lon1, lat2, lon2):
    #             from geopy.distance import geodesic
    #             return geodesic((lat1, lon1), (lat2, lon2)).km

    #         distance = calculate_distance(source_lat, source_lon, destination_lat, destination_lon) if source_lat and destination_lat else None

    #         # Prepare context for rendering
    #         context = {
    #             'form': form,
    #             'ride': ride,
    #             'source_address': source_address,
    #             'destination_address': destination_address,
    #             'source_lat': source_lat,
    #             'source_lon': source_lon,
    #             'destination_lat': destination_lat,
    #             'destination_lon': destination_lon,
    #             'distance': distance
    #         }

    #         # Optionally, you can get all rides and the latest ride
    #         rides = mapRider.objects.all()
    #         for ride in rides:
    #             print(f"Ride Details: Source - {ride.source}, Destination - {ride.destination}")
            
    #         latest_ride = mapRider.objects.latest('id')
    #         print(f"Last ride added: Source - {latest_ride.source}, Destination - {latest_ride.destination}")

    #         # Render the map page with route information
    #         return render(request, 'map_user.html', context)

    # else:
    #     form = mapRiderForm()

    # # Render the map page with an empty form for GET requests
    # return render(request, 'map_user.html', {'form': form})

   


def online_redirect(request):
    # Redirect to the desired page when the "Online" button is clicked
    return redirect('matching_passengers')  # Replace 'next_page' with your actual URL name


def matching_passengers(request):
    return render(request, 'matching_passengers.html')

def online_redirect1(request):
    # Redirect to the desired page when the "Online" button is clicked
    return redirect('display_rider') 

#def display_rider(request):
    #return render(request, 'display_rider.html')


def preference(request):
    if request.method == 'POST':
        # Retrieve the selected preference from the form
        preference = request.POST.get('preference')
        # Store the preference in the session
        request.session['preference'] = preference
        # Redirect to the same page to display the preference
        return redirect('user_path')
    else:
        # Retrieve the preference from the session for display
        preference = request.session.get('preference', None)
        # Render the form or the result based on whether a preference is selected
        return render(request, 'preference.html', {'preference': preference})
    


def find_matches():
    matches = []
    riders = RiderTrip.objects.all()
    users = UserTrip.objects.all()

    for rider in riders:
        for user in users:
            if (rider.source.strip().lower() == user.source.strip().lower() and 
                rider.destination.strip().lower() == user.destination.strip().lower()):
                matches.append({
                    'rider_source': rider.source,
                    'rider_destination': rider.destination,
                    'user_source': user.source,
                    'user_destination': user.destination
                })
    
    return matches

def display_rider(request):
    if request.method == 'POST':
        form = RiderTripForm(request.POST)
        if form.is_valid():
            # Save the form data
            ride = form.save()

            # Find matches
            matches = find_matches()

            # Render the matches page with the list of matches
            return render(request, 'calculate_fare.html', {'matches': matches, 'form': form})

    else:
        form = RiderTripForm()

    return render(request, 'display_rider.html', {'form': form})


def get_balance(request):
    provider_url = 'HTTP://127.0.0.1:7545'
    w3 = Web3(Web3.HTTPProvider(provider_url))

    # Replace with the Ethereum address you want to check
    address = '0x31cb30897014a7bB94D3c399C63D078E1780501F'
    
    balance_eth = 0
    try:
        # Check if the address is valid
        if not Web3.is_address(address):
            error_message = "Invalid Ethereum address"
        else:
            # Get balance in Wei
            balance_wei = w3.eth.get_balance(address)

            # Convert balance to Ether
            balance_eth = Web3.from_wei(balance_wei, 'ether')

            error_message = None
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
    
    context = {
        'address': address,
        'balance': balance_eth,
        'error_message': error_message,
    }
    return render(request, 'get_balance.html', context)

def calculate_fare(request):
    distance = 0
    fare = 0
    error_message = None

    if request.method == 'POST':
        try:
            distance = float(request.POST.get('distance'))
            fare = distance * 5  # Each kilometer is charged at 5 rupees
        except ValueError:
            error_message = "Please enter a valid distance."
    
    context = {
        'distance': distance,
        'fare': fare,
        'error_message': error_message,
    }
    return render(request, 'payment.html', context)

    
from django.views.decorators.http import require_POST

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

@require_POST
def payment(request):
    fare = request.POST.get('fare')

    # Process the payment here
    # Assuming payment is processed successfully

    # Redirect to the payment_success page
    return redirect('payment_success')


def payment_success(request):
    return render(request, 'payment_success.html')

def rider_balance(request):
    provider_url = 'HTTP://127.0.0.1:7545'
    w3 = Web3(Web3.HTTPProvider(provider_url))

    # Replace with the Ethereum address you want to check
    address = '0xEa926bD59c46Ef77941Decb858807c732136789d'
    
    balance_eth = 0
    try:
        # Check if the address is valid
        if not Web3.is_address(address):
            error_message = "Invalid Ethereum address"
        else:
            # Get balance in Wei
            balance_wei = w3.eth.get_balance(address)

            # Convert balance to Ether
            balance_eth = Web3.from_wei(balance_wei, 'ether')

            error_message = None
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
    
    context = {
        'address': address,
        'balance': balance_eth,
        'error_message': error_message,
    }
    return render(request, 'rider_balance.html', context)












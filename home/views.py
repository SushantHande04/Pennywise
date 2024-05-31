from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from home.models import addcash
from home.models import user_info


def home(request):
    #first check if user is authenticated 
    if request.user.is_authenticated:
        if request.method == "POST" and 'addexpense' in request.POST:
            purpose = request.POST['purpose']
            category = request.POST['category']
            amount = request.POST['amount']
            date = request.POST['date']
            instance = addcash(
                user = request.user, 
                purpose=purpose, 
                category=category,
                amount=amount,
                date=date
            )
            instance.save()

        user_i = user_info.objects.get(user=request.user)
        if request.method == "POST" and 'getincome' in request.POST:
            print(request.POST)
            inc = request.POST['gincome']
            user_i.income = int(inc)
            user_i.save()
            
        u = User.objects.get(first_name = request.user.first_name, last_name = request.user.last_name)
        
        table_info = addcash.objects.filter(user = request.user)
        food = 0
        bill = 0
        shopping = 0
        stationary = 0
        for i in table_info:
            if i.category == "food":
                food += i.amount    
            elif  i.category == "bills":
                bill += i.amount
            elif  i.category == "shopping":
                shopping += i.amount
            else:
                stationary += i.amount
        addcash_data = {"food":food, "bill":bill, "shopping": shopping, "stationary":stationary}
        print(food, bill, shopping, stationary)
        expenditure = food + bill + shopping + stationary
        return render(request, 'home.html', {"table_info":table_info,"addcash_data" : addcash_data,"u":u,"user_i": user_i,  "expenditure": expenditure})
    else: #if not authenticated redirect user to signin page
        return redirect('/signin')

def landingpage(request):
    return render(request, 'land.html')

def signup(request):
    if request.method == "POST":
        #variables for storing new user credentials 
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        em = request.POST['email']
        pwd = request.POST['pass']
        c_pwd = request.POST['cpass']
        income = request.POST['income']

        #check for password
        if pwd == c_pwd:
            user = User.objects.create_user(username = uname, first_name = fname, last_name = lname, email = em, password = pwd)
            user.save()
            login(request, user)
            inst = user_info(
                user = request.user,
                income = income
            )
            inst.save()
            return redirect('/home')
        else: 
            return redirect('/signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            # variables to store old user credentials for later comparison
            uname = request.POST['username']
            em = request.POST['email']
            pwd = request.POST['password']
            #compare user credentials with existing instance in database
            user = authenticate(username = uname, email = em, password = pwd)
            if user is not None:
                login(request, user)
                return redirect('/home') #if user exists navigate to homepage
            else:
                return redirect('/signin')
        else:
            return render(request, 'signin.html')
    
def signout(request):
    logout(request)
    return redirect('/signin')
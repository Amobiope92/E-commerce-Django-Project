# from django.shortcuts import redirect, render
# from . forms import signupforms, log_in
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from . forms import log_in, UserRegForm, change_password, ProductCreateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .models import product
from django.contrib.auth.decorators import login_required

# Create your views here.

def signUp(request):

    form = UserRegForm() 

    if request.method == "POST":
        form = UserRegForm(request.POST)  

        if form.is_valid():
            form.save()
            messages.success(request, "User successfully created")
            return redirect('Home')
        else:
            # Capture and pass username error message to template
            username_error = form.errors.get('username')
            email_error = form.errors.get('email')
            if username_error:
                messages.error(request, username_error)
            elif email_error:
                messages.error(request, email_error)
            return redirect('SignUp')
   



# def signUp(request):
#     form = signupforms()

#     if request.method == 'POST':
#         username = request.POST ['username']
#         first_name = request.POST ['first_name']
#         last_name = request.POST ['last_name']
#         email = request.POST ['email']
#         password = request.POST ['password']
#         confirm_password = request.POST ['confirm_password']

#         if password == confirm_password:
#             new_user = User.objects.create_user(
#                 username = username,
#                 first_name= first_name,
#                 last_name= last_name,
#                 email= email
#             )
#             new_user.set_password(password)
#             new_user.save()
#             return redirect('Login')


    context = {
        'form':form
    }
    return render(request, 'Registration/signup.html', context)

def Login(request):
    form = log_in()
    if request.method == 'POST':
        users = request.POST
        user_name = users['username']
        l0gin_password = users['password']

        user = authenticate(request, username = user_name, password = l0gin_password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            invalid_credentials = True 
    
        context = {
        'invalid_credentials': invalid_credentials,
        'form':form 
        
        }
        
        return render(request, 'Registration/login.html', context)
    else:
        context={
          'form':form   
        }
        return render(request, 'Registration/login.html', context)




def Logout(request):
    logout(request)
    return redirect('Home')

class PasswordChangeView(PasswordChangeView):
    form_class = change_password
    success_url = reverse_lazy("password_success")

# def password_success(request):
#     return render(request, "registration/password_success.html" )    
@login_required
def productUpload(request):

    form = ProductCreateForm() 

    if request.method == "POST":
        form = ProductCreateForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully uploaded")
            return redirect('Upload_product')

    context = {'form':form}
            
    return render(request, 'Registration/product_upload.html', context)
@login_required
def view_productUpload(request):
  data = product.objects.all()  
  context = {'data': data}
  return render(request, 'Registration/produpld_tab.html', context)




def modify_product(request, productId):
  produc = product.objects.get(product_id=productId)
  if request.method == 'POST':
    form = ProductCreateForm(request.POST, instance=produc)  # Update existing instance
    if form.is_valid():
      form.save()
      return redirect('success_url')  # Redirect to success page
  else:
    form = ProductCreateForm(instance=produc)  # Pre-fill form for GET request
  context = {'form': form}
  return render(request, 'Registration\modify_product.html', context)





def delete_product(request, productId):
    produc = product.objects.get(product_id = productId)
    produc.delete()
    return redirect("Product_upload_table")
    return render(request, "Registration\produpld_tab.html")
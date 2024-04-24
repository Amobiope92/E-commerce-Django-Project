from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views


# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signUp, name = "SignUp"),
    path('login/', views.Login, name = "Login"),
    path('logout/', views.Logout, name = "Logout"),
    path('change_password/', views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name = "change_password"),
    # path('password_success/', views.password_success, name = "password_success"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'registration/reset_password.html'),name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/reset_password_done.html'),name = "reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/reset_password_confirm.html'),name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/reset_password_complete.html'),name = "reset_password_complete"),
    path('product_upload/', views.productUpload, name = "Upload_product"),
    path('produpld_tab/', views.view_productUpload, name = "Product_upload_table"),
    path('modify_product/<int:productId>/', views.modify_product, name='modify_product_table'),
    path('delete_product/<int:productId>/', views.delete_product, name = "delete_product_table"),
   
]







# urlpatterns = [
#     path('signUp/', views.signUp, name= 'SignUp'),

#     path('Login/', views.Login, name= 'Login'),

#     path('Logout/', views.Logout, name= 'Logout'),

#     path('change_password/', views.PasswordChangeView.as_view(template_name='Registration/password_change.html'), name = "change_password"),
    
#     # path('password_success/', views.password_success, name = "password_success"),

#     path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'Registration/reset_password.html'), name = 'reset_password'),


#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'Registration/reset_password_done.html'), name = "reset_password_done"),


#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Registration/reset_password_confirm.html'), name = "reset_password_confirm"),


#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Registration/reset_password_complete.html'), name = "reset_password_complete"),

# ]
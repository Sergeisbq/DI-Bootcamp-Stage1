from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from image_share.views import ProfileView, SignUpView, profile_redirect_view, update_profile, index_view, upload_image, images_view, user_images
from django.conf import settings
from django.conf.urls.static import static
app_name = 'image_share'


urlpatterns = [
    path('image_share/home/', index_view, name='home'),
    path('registration/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registration/logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('registration/profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('registration/signup/', SignUpView.as_view(), name='signup'),
    path('registration/update-profile/', update_profile, name='update-profile'),
    path('registration/profile-redirect/', profile_redirect_view, name='profile-redirect'),
    path('image_share/upload_image/', upload_image, name='upload_image'),
    path('image_share/view_images/', images_view, name='view_images'),
    path('image_share/user_images/', user_images, name='user_images'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
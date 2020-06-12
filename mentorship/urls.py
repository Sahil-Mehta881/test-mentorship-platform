from django.contrib import admin
from django.urls import path, include

# from dashboard import views
# from startups_listing import views
# from create_startup import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('startups/', include('startups_listing.urls')),
    # path('create_startup/', include('startups_listing.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('mentors/', include('mentors.urls'))

]

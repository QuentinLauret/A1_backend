from django.contrib import admin
from django.urls import path
from guitar_shop import views

urlpatterns = [                 #Link the views to the app
    path('admin/', admin.site.urls),
    path("guit", views.guit),
    path("listing", views.listing),
    path("edit/<int:id>", views.edit),   #Link the app to the view "edit" with an argument : id
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.destroy)
]

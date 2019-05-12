# Simply declaring to which URL path the user will go to depending on the folder selected
# Rendering a view depending on the path

from django.contrib import admin
from django.urls import path

from pins.views import pins_view,jsontodb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pins_view),
    path('jsontodb/',jsontodb)
]

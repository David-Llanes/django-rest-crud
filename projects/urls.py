from django.urls import path, include
from rest_framework import routers
from .api import ProjectViewSet

# TODO Usando Django Rest Framework no es necesario que manualmente creamos las rutas con urlpatters y path.
# TODO En su lugar, Rest Framework nos da un modulo espacial (routers) para crear las rutas CRUD.

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls


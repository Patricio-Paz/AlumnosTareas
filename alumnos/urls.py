from rest_framework.routers import DefaultRouter
from .views import TareaViewSet,AlumnoViewSet

router = DefaultRouter()

router.register(r'Tarea',TareaViewSet, basename='tarea')
router.register(r'Alumno',AlumnoViewSet,basename='alumno')

urlpatterns=router.urls

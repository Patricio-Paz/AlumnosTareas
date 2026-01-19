from rest_framework import viewsets
from .models import Tarea,Alumno
from .serializer import TareaSerializers,AlumnoReadSerializers,AlumnoWriteSerializers

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class=TareaSerializers
    
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return AlumnoReadSerializers # para el get
        return AlumnoWriteSerializers    # para el post,put,delete
    
    
    
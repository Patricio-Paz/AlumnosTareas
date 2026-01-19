from rest_framework import serializers

from.models import Tarea,Alumno


class TareaSerializers(serializers.ModelSerializer):# creando clase que hereda de serializerss
    
    class Meta:
        model= Tarea
        fields= '__all__'

class AlumnoReadSerializers(serializers.ModelSerializer):
    tarea=TareaSerializers(many=True)# indico que serealizre 
    class Meta:
        model=Alumno
        fields='__all__'
    

class AlumnoWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Alumno
        fields='__all__'
    
    def create(self, validated_data):
        tareas=validated_data.pop('tarea',[])
        alumno=Alumno.objects.create(**validated_data)
        alumno.tarea.set(tareas)
        
        return alumno
    def update(self, instance, validated_data):
        tareas =validated_data.pop('tarea',[])
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        if tareas:
            instance.tarea.set(tareas)
        return instance
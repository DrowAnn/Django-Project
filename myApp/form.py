from django import forms

class createNewTask(forms.Form):
    name = forms.CharField(label = "Nombre de la Tarea", max_length = 200)
    description = forms.CharField(widget = forms.Textarea, label = "Descripcion tarea")
    projectId = forms.IntegerField(label = "Id del proyecto asociado")
    
class createNewProject(forms.Form):
    name = forms.CharField(label = "Nombre del Projecto ", max_length = 200)
# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from historial_madre_models import HistorialMadre
from familiars_models import Familiar
from models import Paciente
import datetime
#from django.contrib.auth.models import User



class Ficha_DatosForm(forms.Form):
    SEXO=[('masculino','Masculino'),('femenino','Femenino')]
    GRUPO_SANGUINEO = [('o+','O+'),('o-','O-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-')]
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nacimiento = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker form-control'
                                }))
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect())    
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    lugar_nacimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    grupo_sanguineo = forms.ChoiceField(choices=GRUPO_SANGUINEO, widget=forms.Select(attrs={'class':'form-control'}))

class Ficha_DatosFamiliaresForm(forms.Form):
    ESTUDIO=[('primaria','Primaria'),('secundaria','Secundaria'),('universitaria','Universitaria'),('superior','Superior')]
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    parentesco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nivel_estudio = forms.ChoiceField(choices=ESTUDIO, widget=forms.Select(attrs={'class':'form-control'}))
    #trabajo
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #domicilio
    direccion_domicilio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class Ficha_DatosMedicoForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        

class HistorialMadreForm(ModelForm):
    class Meta:
        model = HistorialMadre
        fields = ['perdidas_gestacionales', 'hijos_muertos', 'num_hijos_nacidos_muertos',
                  'num_hijos_nacidos_vivos', 'enfermedades_previas', 'anticonceptivos']

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        exclude = ['descripcion', 'historial_madre', 'gestacion', 'nacimiento', 'medico']

class MadreForm(ModelForm):
    class Meta:
        model = Familiar
        exclude = ['tipo']

class PadreForm(ModelForm):
    class Meta:
        model = Familiar
        exclude = ['tipo']

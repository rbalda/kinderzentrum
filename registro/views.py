from django.shortcuts import render, render_to_response
from registro.forms import *#Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext

# Create your views here.
def registro_view(request):
    mensaje = ""
    if request.method == "POST":
        mensaje = "guardando datos"
    else:
        mensaje = "enviando forma"
    #datos 
    datos = Ficha_DatosForm()
    datos_familia = Ficha_DatosFamiliaresForm()
    datos_medico = Ficha_DatosMedicoForm()
    historial_madre = HistorialMadreForm()
    paciente = PacienteForm()
    ctx = {'ficha_datos_medico_form':datos_medico,'ficha_datos_familia_form':datos_familia,
           'ficha_datos_form':datos, 'historial_madre_form': historial_madre, 'paciente': paciente,
           'mensaje':mensaje}
    return render_to_response('registro/registro_ficha_medica.html',ctx,context_instance=RequestContext(request))

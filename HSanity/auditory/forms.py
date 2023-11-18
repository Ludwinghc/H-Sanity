from django import forms

class FileUploadForm(forms.Form):
    RNT = forms.FileField(label='Comprobante de inscripción en el RNT', required=False)
    RUT = forms.FileField(label='Comprobante de inscripción al RUT', required=False)
    Registro_Mercantil = forms.FileField(label='Registro Mercantil', required=False)
    Matricula_Mercantil = forms.FileField(label='Matricula Mercantil', required=False)
    Comunicacion_Policia_Nacional = forms.FileField(label='Comunicación Policia Nacional', required=False)
    Uso_de_Suelos = forms.FileField(label='Uso de Suelos', required=False)
    Targeta_Registro_Alojamiento = forms.FileField(label='Targeta Registro Alojamiento', required=False)
    Contrato_Hospedaje = forms.FileField(label='Contrato Hospedaje', required=False)
    Concepto_Tecnico_Bomberos = forms.FileField(label='Concepto Tecnico Bomberos', required=False)
    Concepto_Sanitario = forms.FileField(label='Concepto Sanitario', required=False)
    Permiso_Publicidad = forms.FileField(label='Permiso Publicidad', required=False)
    Sayco_y_Acinpro = forms.FileField(label='Sayco y Acinpro', required=False)
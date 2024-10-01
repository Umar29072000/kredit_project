from django import forms

class KreditForm(forms.Form):
    kontrak_no = forms.CharField(max_length=20)
    client_name = forms.CharField(max_length=100)
    harga_mobil = forms.DecimalField(max_digits=12, decimal_places=2)
    dp_percentage = forms.DecimalField(max_digits=5, decimal_places=2)
    tenor_tahun = forms.IntegerField()
    bunga_tahunan = forms.DecimalField(max_digits=5, decimal_places=2)
    tgl_mulai = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'))

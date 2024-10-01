from django.shortcuts import render
from datetime import date
from dateutil.relativedelta import relativedelta  # Import untuk penghitungan tanggal yang lebih akurat
from .forms import KreditForm

def hitung_kredit(request):
    angsuran_per_bulan = denda_total = total_belum_terbayar = None
    
    if request.method == 'POST':
        form = KreditForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            harga_mobil = data['harga_mobil']
            dp_percentage = data['dp_percentage'] / 100
            tenor_tahun = data['tenor_tahun']
            bunga_tahunan = data['bunga_tahunan'] / 100
            tgl_mulai = data['tgl_mulai']  # Menggunakan date dari form

            # Perhitungan DP dan hutang
            dp = harga_mobil * dp_percentage
            sisa_hutang = harga_mobil - dp
            tenor_bulan = tenor_tahun * 12
            bunga_per_bulan = bunga_tahunan / 12

            # Menghitung angsuran bulanan dengan metode anuitas
            angsuran_per_bulan = (sisa_hutang * bunga_per_bulan) / (1 - (1 + bunga_per_bulan) ** -tenor_bulan)

            # Perhitungan angsuran yang sudah terbayar
            tgl_sekarang = date.today()
            angsuran_terbayar_hingga = (tgl_sekarang.year - tgl_mulai.year) * 12 + (tgl_sekarang.month - tgl_mulai.month)

            # Jika angsuran yang terbayar lebih kecil dari total tenor
            if angsuran_terbayar_hingga < tenor_bulan:
                total_belum_terbayar = angsuran_per_bulan * (tenor_bulan - angsuran_terbayar_hingga)
                
                # Hitung tanggal jatuh tempo terakhir
                tanggal_jatuh_tempo_terakhir = tgl_mulai + relativedelta(months=angsuran_terbayar_hingga)

                # Hitung hari keterlambatan jika sudah melewati tanggal jatuh tempo
                hari_terlambat = (tgl_sekarang - tanggal_jatuh_tempo_terakhir).days

                # Jika sudah lewat tanggal jatuh tempo dan ada keterlambatan
                if hari_terlambat > 0:
                    denda_total = total_belum_terbayar * 0.01 * hari_terlambat
                else:
                    denda_total = 0
            else:
                total_belum_terbayar = 0
                denda_total = 0

        else:
            print(form.errors)  # Debugging jika form tidak valid

    else:
        form = KreditForm()

    return render(request, 'hitung_kredit.html', {
        'form': form,
        'angsuran_per_bulan': angsuran_per_bulan,
        'total_belum_terbayar': total_belum_terbayar,
        'denda_total': denda_total,
    })
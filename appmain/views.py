from django.shortcuts import render


def show_main(request):
    context = {
        'app': 'FasTrack',
        'name': 'Andhika Finnanda Rayhan',
        'class': 'PBP E',
        'cars': [
            {
                'brand': 'BMW',
                'model': 'M3',
                'quantity': 1,
                'engine_spec': '3.0L Twin-turbocharged I6, 473 hp'
            },
            {
                'brand': 'BMW',
                'model': 'X5',
                'quantity': 2,
                'engine_spec': '3.0L Twin-turbocharged I6, 335 hp'
            },
            {
                'brand': 'Mercedes-Benz',
                'model': 'E-Class',
                'quantity': 1,
                'engine_spec': '3.0L Twin-turbocharged V6, 362 hp'
            }
        ]
    }

    return render(request, "main.html", context)

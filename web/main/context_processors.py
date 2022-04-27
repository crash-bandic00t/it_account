from .models import Autozal, Complex

def autozals(request):
    return {
        'autozals': Autozal.objects.all()
    }

def complexes(request):
    return {
        'complexes': Complex.objects.all()
    }
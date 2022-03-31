from .models import Autozal

def autozals(request):
    return {
        'autozals': Autozal.objects.all()
    }
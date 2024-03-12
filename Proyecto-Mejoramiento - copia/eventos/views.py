
from rest_framework import viewsets
from .models import Eventos
from .serializer import EventosSerializer
# Create your views here.
class EventosView(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
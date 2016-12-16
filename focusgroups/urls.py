from django.conf.urls import url, include
from focusgroups.views import *

urlpatterns = [
    url(r'^grupo-nutricional-comunidad/$', grupo_nutricional_comunidad, name='grupo-nutricional-comunidad'),
    url(r'^grupo-nutricional-pais/$', grupo_nutricional_pais, name='grupo-nutricional-pais'),
    url(r'^numero-especies/$', numero_especies, name='numero-especies'),
    url(r'^numero-especies-comunidad/$', numero_especies_comunidad, name='numero-especies-comunidad'),
    url(r'^perfil-especies/$', perfil_especies, name='perfil-especies'),
    url(r'^perfil-especies/(?P<id>\d+)/$', perfil_especies_detalle, name='perfil-especies-detalle'),
    url(r'^perfil-focus-groups/$', perfil_focus_groups, name='perfil_focus_groups'),
    url(r'^perfil-focus-groups/(?P<id>\d+)/$', perfil_focus_groups_detail, name='perfil-focus-groups-detail'),
    url(r'^perfil-abd/$', perfil_abd, name='perfil-abd'),
]

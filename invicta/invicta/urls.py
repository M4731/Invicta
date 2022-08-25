from django.contrib import admin
from django.urls import path, include
from invicta import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #pagina de admin
    path('',views.HomePage.as_view(), name='home'), #pagina index a site-ului
    path('thanks/',views.ThanksPage.as_view(), name='thanks'), #pagina thanks pentru dupa log-out
    path('accounts/',include('accounts.urls', namespace='accounts')), #aplicatia accounts
    path('accounts/',include('django.contrib.auth.urls')), #de aici am luat view-uri pentru logare/autentificare
    path('profiles/',include('profiles.urls', namespace='profiles')),  #aplicatia profiles
    path('teachers',views.ListTeachers.as_view(),name="all_teachers"), #pagina care afiseaza toti profesorii
    path('lessons/',include('lessons.urls', namespace='lessons')), #aplicatia lessons
    path('reviews/',include('reviews.urls', namespace='reviews')), #aplicatia reviews
    path('contact_us',views.ContactFormView.as_view(),name="contact_us"), #form-ul de contact us
    path('thanks_contact/',views.ThanksContactPage.as_view(), name='thanks_contact'), #pagina thanks pentru dupa form-ul de contact us
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #legatura cu fisierele statice
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) #legatura cu fisierele media
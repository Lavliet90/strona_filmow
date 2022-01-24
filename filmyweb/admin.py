from django.contrib import admin
from .models import Ocena, Film, DodatkoweInfo, Aktor

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields= ['tytul', 'opis', 'rok'] #tylko te
    #exclude = ['opis']    #ignor
    list_display = ['tytul', 'imdb_rating', 'rok']  #dlja menu
    list_filter = ('rok',)
    search_fields = ('tytul',) #do szukania


admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)
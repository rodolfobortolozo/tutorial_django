from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline): #admin.StackedInline
    model = Choice
    extra = 3
    
#Personalizar o Formulário Administrador
#Organizar ordem e agrupamentos
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date','id') #Colunas para demostrar no painel administrativo
    list_filter = ['pub_date'] # Filtro
    search_fields = ['question_text'],  #Pesquisa 
    
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Questão', {'fields':['question_text'] }),
        ('Data/Hora', {'fields':['pub_date'] }),
        ]
    inlines = [ChoiceInLine]



admin.site.register(Question, QuestionAdmin)

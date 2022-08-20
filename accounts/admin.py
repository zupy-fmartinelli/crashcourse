from django.contrib import admin

# Register your models here.
# from .models import Customer # Opção para importar apenas um model
from .models import * #coringa para importar todos os modelos de uma vez

# Aqui é a opção para os modelos aparecerem na administração do Django
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
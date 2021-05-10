from django.contrib import admin
import director.models as theater_models

@admin.register(theater_models.Spectacle)
class SpectacleAdmin(admin.ModelAdmin):
    pass

@admin.register(theater_models.Repetition)
class RepetitionAdmin(admin.ModelAdmin):
    pass

@admin.register(theater_models.Actor)
class ActornAdmin(admin.ModelAdmin):
    pass

@admin.register(theater_models.SpectacleActors)
class SpectacleActorsAdmin(admin.ModelAdmin):
    pass

# Register your models here.

from django.contrib import admin
from .models import Profile, Education, Experience, Project, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "location")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("profile", "degree", "school", "start", "end", "order")
    list_filter = ("profile",)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("profile", "role", "company", "start", "end", "order")
    list_filter = ("profile",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "link", "order")
    list_filter = ("profile",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "level", "order")
    list_filter = ("profile",)

from django import forms
from django.forms import inlineformset_factory
from .models import Profile, Education, Experience, Project, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "email", "phone", "location", "summary",
                  "website", "github", "linkedin", "photo"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 4})
        }

EducationFormSet = inlineformset_factory(
    parent_model=Profile,
    model=Education,
    fields=["school", "degree", "start", "end", "details", "order"],
    extra=2,
    can_delete=True
)

ExperienceFormSet = inlineformset_factory(
    parent_model=Profile,
    model=Experience,
    fields=["company", "role", "start", "end", "bullets", "order"],
    widgets={"bullets": forms.Textarea(attrs={"rows": 3})},
    extra=2,
    can_delete=True
)

ProjectFormSet = inlineformset_factory(
    parent_model=Profile,
    model=Project,
    fields=["name", "link", "description", "tech", "order"],
    widgets={"description": forms.Textarea(attrs={"rows": 2})},
    extra=2,
    can_delete=True
)

SkillFormSet = inlineformset_factory(
    parent_model=Profile,
    model=Skill,
    fields=["name", "level", "order"],
    extra=4,
    can_delete=True
)

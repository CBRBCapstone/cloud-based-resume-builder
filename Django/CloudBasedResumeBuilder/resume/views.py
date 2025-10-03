from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import (
    ProfileForm, EducationFormSet, ExperienceFormSet, ProjectFormSet, SkillFormSet
)

def home(request):
    # Use the first profile or create one
    p = Profile.objects.first()
    if not p:
        p = Profile.objects.create(full_name="Your Name", email="you@example.com")
    return redirect("edit_profile", pk=p.pk)

def edit_profile(request, pk):
    p = get_object_or_404(Profile, pk=pk)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=p)
        ed_fs = EducationFormSet(request.POST, instance=p, prefix="ed")
        ex_fs = ExperienceFormSet(request.POST, instance=p, prefix="ex")
        pr_fs = ProjectFormSet(request.POST, instance=p, prefix="pr")
        sk_fs = SkillFormSet(request.POST, instance=p, prefix="sk")

        if (form.is_valid() and ed_fs.is_valid() and ex_fs.is_valid()
                and pr_fs.is_valid() and sk_fs.is_valid()):
            form.save()
            ed_fs.save()
            ex_fs.save()
            pr_fs.save()
            sk_fs.save()
            return redirect("preview", pk=p.pk)
    else:
        form = ProfileForm(instance=p)
        ed_fs = EducationFormSet(instance=p, prefix="ed")
        ex_fs = ExperienceFormSet(instance=p, prefix="ex")
        pr_fs = ProjectFormSet(instance=p, prefix="pr")
        sk_fs = SkillFormSet(instance=p, prefix="sk")

    return render(request, "resume/edit.html", {
        "form": form,
        "ed_fs": ed_fs,
        "ex_fs": ex_fs,
        "pr_fs": pr_fs,
        "sk_fs": sk_fs,
        "profile": p
    })

def preview(request, pk):
    p = get_object_or_404(Profile, pk=pk)
    return render(request, "resume/preview.html", {"p": p})

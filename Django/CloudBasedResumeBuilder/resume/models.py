from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=120, blank=True)
    summary = models.TextField(blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return self.full_name

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="education")
    school = models.CharField(max_length=160)
    degree = models.CharField(max_length=160, blank=True)
    start = models.CharField(max_length=20, blank=True)  # e.g., “Aug 2023”
    end = models.CharField(max_length=20, blank=True)
    details = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experience")
    company = models.CharField(max_length=160)
    role = models.CharField(max_length=160)
    start = models.CharField(max_length=20, blank=True)
    end = models.CharField(max_length=20, blank=True)
    bullets = models.TextField(blank=True, help_text="One bullet per line")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=160)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    tech = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=80)
    level = models.CharField(max_length=40, blank=True)  # e.g., “Advanced”
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

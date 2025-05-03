from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    location_lost = models.CharField(max_length=100)
    date_lost = models.DateField()
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    location_found = models.CharField(max_length=100)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Match(models.Model):
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE)
    confidence_score = models.FloatField()
    match_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Lost: {self.lost_item.title} ↔ Found: {self.found_item.title} ({self.confidence_score}%)"


class Claim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=(('lost', 'Lost'), ('found', 'Found')))
    item_id = models.IntegerField()
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')))
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_claims')

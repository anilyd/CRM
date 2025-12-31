from django.db import models

# Change 'HubData' to 'HubContent' here
class HubContent(models.Model): 
    CATEGORIES = (
        ('tech', 'Technology'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hub_images/')
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.title
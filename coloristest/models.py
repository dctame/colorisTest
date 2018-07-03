from django.db import models

class Post(models.Model):
    text = models.TextField()
    words = str(text)
    words = words.split()
    output = []
    for x in words:
        if x not in output:
            output.append(x)
    lenght = len(output)
            
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.text
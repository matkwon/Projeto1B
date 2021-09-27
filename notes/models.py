from django.db import models


class Tag(models.Model):
    nome = models.TextField()

    def __str__(self):
        return str(self.nome)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id) + ". " + str(self.title)
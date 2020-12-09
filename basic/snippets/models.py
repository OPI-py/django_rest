from django.db import models


LANGUAGE_CHOICES = (("e", "English"), ("u", "Ukrainian"), ("p", "Polish"))
STYLE_CHOICES = (("f", "Formal"), ("i", "Informal"))


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default="English",
    	max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default="Formal",
    	max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets',
    	on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
    	linenos = 'table' if self.linenos else False
    	options = {'title': self.title} if self.title else {}
    	super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
    	return f"{self.title}, {self.owner}"

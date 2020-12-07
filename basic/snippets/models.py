from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


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
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
    	# lexers = get_lexer_by_name(self.language)
    	linenos = 'table' if self.linenos else False
    	options = {'title': self.title} if self.title else {}
    	# formatter = HtmlFormatter(style=self.style, linenos=linenos,
    		# full=True, **options)
    	# self.highlighted = highlight(self.code, lexer, formatter)
    	super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
    	return f"{self.title}, {self.owner}"

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LANGUAGE_CHOICES = sorted([(item[1][0], item[0])for item in get_all_lexers()])
STYLE_CHOICES = sorted((item,item) for item in list(get_all_styles()))

class Snippet( models.Model ):
    created  = models.DateTimeField(auto_now_add=True)
    title    = models.CharField(max_length=100, default='')
    code     = models.TextField()
    linenos  = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, 
                                default='python',
                                max_length=100)
    style    = models.CharField(choices=STYLE_CHOICES, 
                                default='friendly',
                                max_length=100)
    
    class Meta:
        ordering = ('created',)
        
 
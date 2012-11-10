from django.forms import widgets
from rest_framework import serializers
from snippets import models

class SnippetSerializer( serializers.ModelSerializer ):
    """
    Here we take advangage of the ModelSerializer ( analogous to the ModelForm )
    """
    class Meta:
        model = models.Snippet
        fields = ( 'id', 'title', 'code', 'linenos', 'language', 'style' )

#class SnippetSerializer( serializers.Serializer ):
#    """
#    Here we expliclitly define all of the fields
#    """
#    pk       = serializers.Field() # Note: 'Field' is an untpyed read-only field.
#    
#    title    = serializers.CharField(required=False, max_length=100)
#    
#    code     = serializers.CharField(widget=widgets.Textarea, max_length=10000)
#    
#    linenos  = serializers.BooleanField(required=False)
#
#    language = serializers.ChoiceField(choices=models.LANGUAGE_CHOICES, 
#                                       default='python')
#
#    style    = serializers.ChoiceField(choices=models.STYLE_CHOICES, 
#                                       default='friendly')
#    
#    def restore_object( self, attrs, instance=None ):
#        """
#        Create or update a new snippet instance.
#        """
#        if instance:
#            # updating existing instance
#            instance.title = attrs['title']
#            instance.code = attrs['code']
#            instance.linenos = attrs['linenos']
#            instance.language = attrs['language']
#            instance.style = attrs['style']
#            return instance
#        
#        # create new instance
#        return models.Snippet(**attrs)
    
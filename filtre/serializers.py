#represente data sous format Json
#on represente les model sous format json
from rest_framework import serializers
from .models import *
# pour chaque class on fait le modelserializers
#ModelSerializer me permet de faire les operation crud sur la classe automatiquement
class DivisionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class Profit_centerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profit_center
        fields = '__all__'

class OrganisationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class RangeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'



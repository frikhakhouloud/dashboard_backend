#represente data sous format Json
#on represente les model sous format json
from rest_framework import serializers
from .models import *
# pour chaque class on fait le modelserializers
#ModelSerializer me permet de faire les operation crud sur la classe automatiquement
class Order_filesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_files
        fields = '__all__'


class Order_past_per_divsionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_past_per_divsion
        fields = '__all__'

class Order_past_per_organismeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_past_per_organisme
        fields = '__all__'


class Order_past_per_cpSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_past_per_cp
        fields = '__all__'


class Order_past_per_errorsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order_past_per_errors
        fields = '__all__'

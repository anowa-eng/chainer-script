from rest_framework import serializers

class SceneHeaderSerializer(serializers.Serializer):
    class Meta:
        fields = ['__all__']
class ActionEventSerializer(serializers.Serializer):
    class Meta:
        fields = ['__all__']
class DialogEventSerializer(serializers.Serializer):
    class Meta:
        fields = ['__all__']
class TransitionEventSerializer(serializers.Serializer):
    class Meta:
        fields = ['__all__']
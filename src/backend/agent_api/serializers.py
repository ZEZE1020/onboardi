from rest_framework import serializers

class AgentRequestSerializer(serializers.Serializer):
    goal = serializers.CharField()

class AgentResponseSerializer(serializers.Serializer):
    steps = serializers.ListField(child=serializers.CharField())

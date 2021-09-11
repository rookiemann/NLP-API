class FLIPSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, default='')
    code = serializers.CharField(max_length=25000, default='')
    categories = serializers.JSONField(default = dict)
    sentences = serializers.JSONField(default = dict)

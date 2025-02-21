from rest_framework import serializers
from .models import TextAnalysis

class TextAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnalysis
        fields = ['id', 'original_text', 'processed_text', 'analysis_type', 'created_at']
        read_only_fields = ['id', 'created_at']
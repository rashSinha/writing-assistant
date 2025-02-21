from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TextAnalysis
from .serializers import TextAnalysisSerializer
from openai import OpenAI
from decouple import config

class TextAnalysisViewSet(viewsets.ModelViewSet):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TextAnalysis.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def process_text(self, request):
        text = request.data.get('text')
        action = request.data.get('action', 'summarize')
        
        client = OpenAI(api_key=config('OPENAI_API_KEY'))
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant. Perform the following action on the text: {action}"},
                    {"role": "user", "content": text}
                ]
            )

            processed_text = response.choices[0].message.content

            # Create and save analysis
            analysis = TextAnalysis.objects.create(
                user=request.user,
                original_text=text,
                processed_text=processed_text,
                analysis_type=action
            )

            serializer = self.get_serializer(analysis)
            return Response(serializer.data)
        
        except Exception as e:
            return Response({'error': str(e)}, status=400)
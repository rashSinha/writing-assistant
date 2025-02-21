from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from openai import OpenAI
from decouple import config
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

client = OpenAI(api_key=config('OPENAI_API_KEY'))

@login_required
def process_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        action = request.POST.get('action')

        try:
            if action == 'tone_detection':
                # Sentiment analysis using TextBlob
                blob = TextBlob(text)
                sentiment_score = blob.sentiment.polarity

                # Advanced sentiment analysis
                sia = SentimentIntensityAnalyzer()
                nltk_sentiment = sia.polarity_scores(text)

                # OpenAI enhanced tone analysis
                tone_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Analyze the emotional tone of the following text"},
                        {"role": "user", "content": text}
                    ]
                )

                processed_text = tone_response.choices[0].message.content

                # Save analysis
                analysis = TextAnalysis.objects.create(
                    user=request.user,
                    original_text=text,
                    processed_text=processed_text,
                    analysis_type='tone_detection'
                )

                return JsonResponse({
                    'status': 'success',
                    'result': processed_text,
                    'sentiment_score': sentiment_score,
                    'nltk_sentiment': nltk_sentiment
                })
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant. Perform the following action on the text: {action}"},
                    {"role": "user", "content": text}
                ]
            )

            processed_text = response.choices[0].message.content

            # Save to database
            analysis = TextAnalysis.objects.create(
                user=request.user,
                original_text=text,
                processed_text=processed_text,
                analysis_type=action
            )

            return JsonResponse({
                'status': 'success',
                'result': processed_text
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })

    return render(request, 'writer/index.html')

@login_required
def analysis_history(request):
    analyses = TextAnalysis.objects.filter(user=request.user)
    return render(request, 'writer/history.html', {'analyses': analyses})
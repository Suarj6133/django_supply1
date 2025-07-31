from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required  
from django.views.decorators.csrf import csrf_exempt  # ✅ use this now
import json
from .models import WeeklySummary
from django.db.models import Sum

# Intro and Weekly Views
@login_required
def intro(request):
    return render(request, 'dashboard/intro.html')

@login_required
def wk01(request):
    return render(request, 'dashboard/wk01.html')

@login_required
def wk02(request):
    return render(request, 'dashboard/wk02.html')

@login_required
def wk03(request):
    return render(request, 'dashboard/wk03.html')

@login_required
def performance(request):
    return render(request, 'dashboard/performance.html')

# ✅ Save weekly summary without CSRF requirement
@csrf_exempt  # 🔥 CSRF protection is now disabled for this view
@login_required
def save_weekly_summary(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            week = data.get('week')
            revenue = data.get('revenue')
            profit = data.get('profit')
            expense = data.get('expense')
            print("Received data:", data)

            WeeklySummary.objects.update_or_create(
                user=request.user,
                week=week,
                defaults={
                    'revenue': revenue,
                    'expense': expense,
                    'profit': profit,
                }
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print("Error saving summary:", e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'invalid method'}, status=400)


#performance 
@login_required
def performance(request):
    totals = WeeklySummary.objects.filter(user=request.user).aggregate(
        total_revenue=Sum('revenue'),
        total_expense =Sum('expense'),
        total_profit=Sum('profit')
    )

    return render(request, 'dashboard/performance.html',{
        'totals':totals,
    })
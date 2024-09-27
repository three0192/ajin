from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime
import random

def index(request):
    now = datetime.now()
    context = {
        'current_time' : now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    # 사용자로부터 입력받은 6개의 로또 번호
    chosen_numbers = [
        int(request.GET.get('number1')),
        int(request.GET.get('number2')),
        int(request.GET.get('number3')),
        int(request.GET.get('number4')),
        int(request.GET.get('number5')),
        int(request.GET.get('number6'))
    ]

    # 1~45 사이에서 random_count만큼의 랜덤한 번호 생성
    # 항상 6개의 숫자를 생성
    generated_numbers = random.sample(range(1, 46), 6)
    generated_numbers.sort()

    matching_numbers = len(set(chosen_numbers) & set(generated_numbers))

    # 등수 판별
    if matching_numbers == 6:
        rank = "1등"
    elif matching_numbers == 5:
        rank = "2등"
    elif matching_numbers == 4:
        rank = "3등"
    else:
        rank = "꽝"

    context = {
        'chosen': chosen_numbers,
        'numbers': generated_numbers,
        'isValid': f"입력된 번호와 추천 번호를 확인하세요. 결과는 {rank}입니다.",
        'rank': rank
    }
    
    return render(request, 'first/result.html', context)
    


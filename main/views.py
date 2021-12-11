from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from model.motivation_classification import predict

def index(request):
    context={'a': 'Hello'}
    return render(request, 'index.html', context)

@require_POST
@csrf_exempt
def classifyMotivation(request):
    print(request.POST.get('value'))
    sentence = request.POST.get('value')
    result = predict(sentence)
    print("ini result ", result)
    if(result[0]==1):
        desc = 'rendah'
    elif(result[0]==2):
        desc = 'sedang'
    else:
        desc = 'tinggi'
    context={'result': desc}
    return render(request, 'index.html', context)
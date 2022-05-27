from django.shortcuts import render

# Create your views here.
def displayHomePage(request):
    return render(request,'home.html')
def showquestions(request):
    return render(request,'questions.html')    
def showresult(request):
    ans1=request.GET['q1']
    ans2=request.GET['q2']
    ans3=request.GET['q3']
    ans4=request.GET['q4']
    ans5=request.GET['q5']
    score=0
    totalscore=20
    correct=0
    wrong=0
    if ans1=='3':
        score+=4
        correct+=1
    else:
        score-=1
        wrong+=1
    if ans2=='4':
        score+=4
        correct+=1
    else:
        score-=1
        wrong+=1
    if ans3=='2':
        score+=4
        correct+=1
    else:
        score-=1
        wrong+=1
    if ans4=='2':
        score+=4
        correct+=1
    else:
        score-=1
        wrong+=1
    if ans5=='1':
        score+=4
        correct+=1
    else:
        score-=1
        wrong+=1
    result=score/totalscore*100
    print(f'score is {score}/{totalscore} and percentage is {result}')    
    res=''
    if result>=70:
        res='CONGRATULATIONS YOU PASSED THE TEST'
    else:
        res="YOU COULDN'T PASS THE TEST THIS TIME"    
    return render(request,'result.html',{'result':result,'score':score,'maxmarks':totalscore,'remarks':res,'correct':correct,'wrong':wrong})
def showthankupage(request):
    return render(request,'thanks.html')    

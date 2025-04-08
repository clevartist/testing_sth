from django.views import View
from django.shortcuts import render, redirect
from .utils import postCabinet

draft = {
    "title": "",
    "requires_questions": False,
    "questions": {}
}

class Home(View):
    def get(self, request):
        return render(request, "home.html")

class BuildCabinet(View):
    def get(self, request):
        return render(request, "buildCabinet.html")
    
    def post(self, request):
        title = request.POST.get("title")
        requires_questions = "requires_questions" in request.POST # only if it's checked

        draft.update({"title": title})
        print(draft["title"])

        if requires_questions:
            return redirect('buildQuestion')
        
        postCabinet(draft["title"], draft["requires_questions"])

        return redirect('home')

class BuildQuestion(View):
    def get(self, request):
        return render(request, "buildQuestion.html")
    
    def post(self, request):
        question_title = request.POST.get("question_title")
        
        draft["questions"].update({"question_title": question_title})
        postCabinet(draft["title"], draft["requires_questions"], draft["questions"]["question_title"])

        return redirect('home')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Members, Ratings
from .create_graph import create_rating_graph


def index(request):
    return render(request,'visualizer/index.html')


def user_search(request):
    return render(request,'visualizer/user_search.html')


def user_search_result(request):
    if request.method == 'GET':
        return render(request,'404.html')
    query_name = request.POST['name_alphabet']
    result = []
    
    if len(query_name) == 0 :
        return render(request,'visualizer/fill_in_the_query.html')
    else:
        query_result = Members.objects.filter(name_alphabet__icontains=query_name)
        for qr in query_result:
            result.append({"name_alphabet":qr.name_alphabet,"ncs_id":qr.ncs_id})
        
        query_result = Members.objects.filter(ncs_id__icontains=query_name)
        for qr in query_result:
            result.append({"name_alphabet":qr.name_alphabet,"ncs_id":qr.ncs_id})
            
        context = {"result":result}
        
        return render(request,'visualizer/user_search_result.html',context)


def user_index(request,ncs_id):
    user_name = Members.objects.filter(ncs_id=ncs_id)
    if len(user_name) is 0:
        return render(request,'404.html')
    else:
        context = {"name_alphabet": user_name.get().name_alphabet,
                   "ncs_id": user_name.get().ncs_id}
        
        user_data = Ratings.objects.filter(ncs_id=ncs_id).order_by('update_month')
        
        context["rating_history"] = [{"update_month": ud.update_month.strftime("%Y-%m"),
                                      "rating": ud.rating} for ud in user_data]
        
        context["filename"] = create_rating_graph(context["rating_history"])
        
        return render(request,'visualizer/user_index.html',context)
    

def ranking(request):
    context = {}
    rating_list = []
    resolved_list = []
    latest_month = Ratings.objects.all().order_by('-update_month')[0].update_month
    q = Ratings.objects.filter(update_month=latest_month)
    for r in q:
        rating_list.append({"rating":r.rating,"ncs_id":r.ncs_id})
    rating_list.sort(key=lambda t:(-t["rating"],t["ncs_id"]))
    
    for i,rl in enumerate(rating_list):
        resolved_list.append({"rank": i+1,
                              "name_alphabet":Members.objects.filter(ncs_id=rl["ncs_id"]).get().name_alphabet,
                              "rating":rl["rating"]})
        
    context["rating_list"] = resolved_list
    context["update_month"] = latest_month 
    return render(request, 'visualizer/ranking.html',context)
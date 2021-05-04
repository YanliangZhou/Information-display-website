from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get('http://api.github.com/users?since=0')
    api = json.loads(api_request.content)
    return render(request, 'orders.html', {'api': api})

def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get('http://api.github.com/users/'+user)
        username = json.loads(user_request.content)
        return render(request, 'user.html', {'user': user, 'username': username})
    else:
        notfound = "请输入搜索内容..."
        return render(request, 'user.html', {'notfound': notfound})
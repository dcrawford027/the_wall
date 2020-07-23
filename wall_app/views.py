from django.shortcuts import render, redirect
from login_app.models import User
from .models import Message, Comment
from datetime import *
from dateutil.relativedelta import *

# Create your views here.
def wall(request):
        
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Message.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, 'wall.html', context)

def postMessage(request):
    user = User.objects.get(id=request.session['user_id'])
    content = request.POST['mess_content']
    message = Message.objects.create(user_id=user, message=content)
    return redirect('/wall')

def postComment(request):
    user = User.objects.get(id=request.session['user_id'])
    post = Message.objects.get(id=request.POST['post_id'])
    content = request.POST['comment_content']
    comment = Comment.objects.create(message_id=post, user_id=user, comment=content)
    return redirect('/wall')

def deleteMessage(request):
    message = Message.objects.get(id=request.POST['post_id'])
    message.delete()
    return redirect('/wall')
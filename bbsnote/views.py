from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone

def index(request):
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list' : board_list}
    #return HttpResponse("bbsnote에 오신 것을 환영합니다.");
    return render(request,'bbsnote/board_list.html',context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    comment.save()
    return redirect('bbsnote:detail', board_id=board.id)
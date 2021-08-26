from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


@permission_classes((IsAuthenticated))
@login_required
def files(request):
    permissions_classes = [permissions.IsAuthenticated]
    return render(request, 'files.html')

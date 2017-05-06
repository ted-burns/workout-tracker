# -*- coding: utf-8 -*-
#pylint: disable=E1101,C0111,C0301
from __future__ import unicode_literals
from tracker.serializers import MuscleGroupSerializer, MuscleSerializer, UserSerializer, ExerciseSerializer, SetSerializer, WorkoutSerializer
from tracker.models import MuscleGroup, Muscle, User, Exercise, Set, Workout
#from django.shortcuts import render
from rest_framework import viewsets

class MuscleGroupList(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class MuscleList(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExerciseList(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class SetList(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class WorkoutList(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

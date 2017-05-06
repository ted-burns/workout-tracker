# -*- coding: utf-8 -*-
"""
    Model defitions for all of workout tracking items
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class MuscleGroup(models.Model):
    """
    Muscle groups
    """
    name = models.TextField(max_length=100)


class Muscle(models.Model):
    """
    Model for the individual muscles
    Note: Might not be necessary
    """
    name = models.TextField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup)


class Exercise(models.Model):
    """
    Model for individual exercises
    """
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    muscles = models.ManyToManyField(Muscle)


class Workout(models.Model):
    """
    Model for workouts
    """
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    focus = models.ForeignKey(MuscleGroup)


class Set(models.Model):
    """
    Model for sets as a part of workouts
    """
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    expected_reps = models.IntegerField()
    performed_reps = models.IntegerField(null=True)
    order = models.IntegerField(null=True)



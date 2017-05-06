"""
V0.1 Serializers for the models
"""
#pylint: disable=C0111,W0232,C1001,R0903
from tracker.models import User, MuscleGroup, Muscle, Exercise, Workout, Set
from rest_framework import serializers

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout


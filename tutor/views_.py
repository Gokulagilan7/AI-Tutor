from django.shortcuts import render
from sklearn.neighbors import NearestNeighbors
import numpy as np
from .models import User, Lesson, UserLessonInteraction

def recommend_lessons(request, user_id):
    interactions = UserLessonInteraction.objects.all()
    users = User.objects.all()
    lessons = Lesson.objects.all()

    user_lesson_matrix = np.zeros((len(users), len(lessons)))

    for interaction in interactions:
        user_index = list(users).index(interaction.user)
        lesson_index = list(lessons).index(interaction.lesson)
        user_lesson_matrix[user_index, lesson_index] = interaction.rating

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(user_lesson_matrix)

    user_index = list(users).index(User.objects.get(id=user_id))
    distances, indices = model.kneighbors(user_lesson_matrix[user_index].reshape(1, -1), n_neighbors=5)

    recommended_lessons = []
    for index in indices[0]:
        recommended_lessons.append(lessons[index])

    return render(request, 'tutor/recommendations.html', {'lessons': recommended_lessons})



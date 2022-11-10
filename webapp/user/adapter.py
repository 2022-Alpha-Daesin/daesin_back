from allauth.account.adapter import DefaultAccountAdapter
from .models import Major, UserMajor
from django.shortcuts import get_object_or_404

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # 추가 저장 필드: nickname, grade, major
        nickname = data.get('nickname')
        grade = data.get('grade')
        major = data.get('major')
        if nickname:
            user.nickname = nickname
        if grade:
            user.grade = grade
        user.save()
        if major:
            major = get_object_or_404(Major, pk=major)
            user_major = UserMajor.objects.create(
                user=user,
                major=major
            )
        return user


from allauth.account.adapter import DefaultAccountAdapter
from .models import Major, UserMajor
from django.shortcuts import get_object_or_404
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # 추가 저장 필드: nickname, grade, major
        nickname = data.get('nickname')
        grade = data.get('grade')
        major_id = data.get('major_id')
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
    
    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_FRONT + \
            'signin/?key=' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
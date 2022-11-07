from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # 추가 저장 필드: major,address, grade
        nickname = data.get('nickname')
        grade = data.get('grade')
        major = data.get('major')
        if nickname:
            user.nickname = nickname
        if grade:
            user.grade = grade
        if major:
            user.major = major
        user.save()
        return user
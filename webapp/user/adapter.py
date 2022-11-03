from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.username = data.get('username')
        user.email = data.get('email')
        user.nickname = data.get('nickname')
        user.grade = data.get('grade')
        user.major = data.get('major')
        user.save()
        return user
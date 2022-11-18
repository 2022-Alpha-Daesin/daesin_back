from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """ModelManager definition for User Model"""

    def create_user(self, email, password):
        """일반 유저 생성 메소드"""
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, email, nickname, password):
        """슈퍼 유저(superuser) 생성 메소드"""
        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'

    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="이메일",
    )
    nickname = models.CharField(
        unique=True,
        max_length=20,
        verbose_name="닉네임",
    )
    grade = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="학년",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="계정 생성 일자"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="계정 수정 일자",
    )

    is_active = models.BooleanField(
        default=True
    )
    # createsuperuser 시 물어 보는 field 추가 (nickname은 null False 이기 때문)
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

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

    def create_superuser(self, email, password):
        """슈퍼 유저(superuser) 생성 메소드"""
        user = self.model(
            email=email,
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
    # username = models.CharField(
    #     unique=True,
    #     max_length=20,
    # )  필수 아니래 얘들아 -강승원
    # 사용자명 (필수)
    email = models.EmailField(
        null=True,
        unique=True,
    )  # 이메일 (필수)
    nickname = models.CharField(
        null=True,
        unique=True,
        max_length=20,
    )  # 닉네임 (필수)
    grade = models.PositiveIntegerField(
        null=True,
        blank=True,
    )  # 학년 (선택)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 유저 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 유저 레코드가 수정된 일자

    is_active = models.BooleanField(
        default=True
        )
    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser
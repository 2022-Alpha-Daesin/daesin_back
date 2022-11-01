from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """ModelManager definition for User Model"""

    def create_user(self, username, password):
        """일반 유저 생성 메소드"""
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, username, password):
        """슈퍼 유저(superuser) 생성 메소드"""
        user = self.model(
            username=username,
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

    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )  # 사용자명
    email = models.EmailField(
        null=True,
        unique=True,
    )  # 이메일
    # TODO nickname unique 로 할 건지 알아보기
    nickname = models.CharField(
        null=True,
        unique=True,
        max_length=20,
    )  # 닉네임
    grade = models.PositiveIntegerField(
        null=True,
        blank=True,
    )  # 학년
    # TODO 전공은 choice 필드로 할 건지 알아보기
    major = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )  # 전공
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 유저 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 유저 레코드가 수정된 일자

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

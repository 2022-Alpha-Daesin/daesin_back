from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """ModelManager definition for User Model"""

    def _create_user(self, username, password, email, **kwargs):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save()

    def create_user(self, username, password, email, **kwargs):
        """일반 유저 생성 메소드"""
        self._create_user(username, password, email, **kwargs)

    def create_superuser(self, username, password, email, **kwargs):
        """슈퍼 유저(superuser) 생성 메소드"""
        kwargs.setdefault('is_superuser', True)
        self._create_user(username, password, email, **kwargs)


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
        unique=True,
    )  # 이메일
    # TODO nickname unique 로 할 건지 알아보기
    nickname = models.CharField(
        unique=True,
        max_length=20,
    )  # 닉네임
    grade = models.PositiveIntegerField(
        blank=True
    )  # 학년
    # TODO 전공은 choice 필드로 할 건지 알아보기
    major = models.CharField(
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

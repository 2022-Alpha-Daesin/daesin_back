from django.db import models

from post.models import Post
from user.models import User


class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="댓글 작성자"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="댓글 다는 글"
    )
    content = models.TextField(
        verbose_name="댓글 내용",
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reply",
        verbose_name="대댓글이 참조하는 댓글",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="댓글 작성 시간",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="댓글 수정 시간",
    )

    def __str__(self):
        return f"{self.content}"

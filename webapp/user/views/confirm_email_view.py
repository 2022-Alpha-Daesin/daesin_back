from rest_framework import status
from rest_framework.response import Response
from dj_rest_auth.registration.views import VerifyEmailView
from django.utils.translation import gettext_lazy as _
from allauth.account.models import EmailAddress, EmailConfirmation, EmailConfirmationHMAC

class ConfirmEmailView(VerifyEmailView):
    
    
    def get_object(self, queryset=None):
        key = self.kwargs["key"]
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                return None
        return emailconfirmation
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        if confirmation == None:
            return Response({'msg':'emailconfirmation does not exist'},status.HTTP_404_NOT_FOUND)
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)



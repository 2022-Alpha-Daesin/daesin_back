from rest_framework.serializers import ModelSerializer

from club.models import Club


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = [
            'id',
            'division',
            'name',
            'intro',
            'curriculum',
            'signup_condition',
            'recruitment_period_start',
            'recruitment_period_end',
            'representative_number',
            'place',
            'members_count',
            'logo',
            'pamphlet',
        ]

from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["full_name", "gender", "institution", "unique_id"]
        read_only_fields: list[str] = ["unique_id"]

from rest_framework import serializers
from users.models import currency_choices

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['user', 'currency', 'amount']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance, given the validated data.
        """
        instance.code = validated_data.get('amount', instance.code)
        instance.save()
        return instance    

class FundMyWallet(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.ChoiceField(choices=currency_choices)


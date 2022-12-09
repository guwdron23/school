from django.forms import ValidationError


def validate_phone_namber(phone_number: str):
    phone_number = phone_number.replace(' ', '')
    if len(phone_number) < 12:
        raise ValidationError('Длина номера не совпадает!')
    if not phone_number.startswith('+'):
        raise ValidationError('Пишите номер в международном формате')
    numbers = '+0987654321'
    for i in phone_number:
        if i not in numbers:
            raise ValidationError(f'Телефонный номер не может содержать "{i}"!')
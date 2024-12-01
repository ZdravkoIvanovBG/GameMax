from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "File needs to be up to 5 MB!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        max_size_bytes = 5 * 1024 * 1024

        if value.size > max_size_bytes:
            raise ValidationError(self.message)

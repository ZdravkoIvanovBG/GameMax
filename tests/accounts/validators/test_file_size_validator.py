from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from GameMax.app_users.validators import MaxFileSizeValidator


class TestFileSizeValidator(TestCase):
    def setUp(self):
        self.validator = MaxFileSizeValidator()

    def test_valid_file_size__expect_no_errors(self):
        small_file = SimpleUploadedFile('small_file.txt', b"a" * (4 * 1024 * 1024))

        try:
            self.validator(small_file)
        except ValidationError:
            self.fail("ValidationError raised unexpectedly")

    def test_invalid_file_size__expect_validation_error(self):
        large_file = SimpleUploadedFile('large_file.txt', b"a" * (6 * 1024 * 1024))

        with self.assertRaises(ValidationError) as e:
            self.validator(large_file)

        self.assertEqual(str(e.exception), "['File needs to be up to 5 MB!']")

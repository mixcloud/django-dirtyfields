import sys
import django


if django.VERSION < (1, 9):
    def get_m2m_with_model(given_model):
        return given_model._meta.get_m2m_with_model()

    def remote_field(field):
        return field.rel
else:
    def get_m2m_with_model(given_model):
        return [
            (f, f.model if f.model != given_model else None)
            for f in given_model._meta.get_fields()
            if f.many_to_many and not f.auto_created
        ]

    def remote_field(field):
        return field.remote_field


if sys.version_info < (3,0,0):
     buffer_type = buffer
else:
     buffer_type = memoryview


def is_buffer(value):
    return isinstance(value, buffer_type)


from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def _has_role(user, role):
    if not user.is_authenticated:
        return False
    if not user.is_active or not getattr(user, role):
        raise PermissionDenied
    return True

def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    Redirects anonymous users to login; denies authenticated users without the role.
    '''
    actual_decorator = user_passes_test(
        lambda u: _has_role(u, 'is_student'),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    Redirects anonymous users to login; denies authenticated users without the role.
    '''
    actual_decorator = user_passes_test(
        lambda u: _has_role(u, 'is_teacher'),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

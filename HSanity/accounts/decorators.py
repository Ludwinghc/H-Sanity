from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticatedUser(view_func):
    def wrapperFunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("auditorHome")
        else:
            return view_func(request, *args, **kwargs)

    return wrapperFunc


def allowedUsers(allowedRoles=[]):
    def decorator(view_func):
        def wrapperFunc(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedRoles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    "You do not have the authority to access this page."
                )

        return wrapperFunc

    return decorator


# def adminOnly(view_func):
#     def wrapperFunc(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'auditor':
#             return redirect('auditorHome')
#         if group == 'user':
#             return view_func(request, *args, **kwargs)
#     return wrapperFunc


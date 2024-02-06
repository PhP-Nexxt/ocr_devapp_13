from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """
    Renders profiles list page with all Profile objects from the database.
    Fetches Profiles, places them into context, and serves the rendered view.

    :param request: http request object.
    :type request: object
    :return: http response with context
    :rtype: tuple[request, html, dict[list[dict]]
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males


def profile(request, username):
    """
    Displays a profile page for a given username.
    Fetches and shows profile details in a template.

    :param request: http request object.
    :type request: object
    :param username: user name.
    :type username: str
    :return: http response with context
    :rtype: tuple[request, html, dict[dict]
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

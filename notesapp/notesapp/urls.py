import debug_toolbar

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import notes.views

import notesapp_auth.views
from django_registration.backends.activation.views import RegistrationView
from notesapp_auth.forms import NotesappRegistrationForm

import flashcards.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes.views.index, name="home"),
    path('flashcards/', flashcards.views.flashcard_index, name="flashcards-index"),
    path("note/<slug>/", notes.views.post_detail, name="notes-detail"),
    path("ip/", notes.views.get_ip),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path(
    "accounts/register/",
    RegistrationView.as_view(form_class=NotesappRegistrationForm),
    name="django_registration_register",
    ),
    path("accounts/profile/", notesapp_auth.views.profile, name="profile"),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("api/v1/", include("notes.api.urls")),
    path("note-table/", notes.views.post_table, name="notes-post-table"),
]

# Map the path __debug__/ to the DJDT's URL's, but only in debug mode.
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

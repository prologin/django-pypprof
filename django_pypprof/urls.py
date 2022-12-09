# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2022 Association Prologin <association@prologin.org>
# Copyright (c) 2022 Marc 'risson' Schmitt <marc.schmitt@prologin.org>

from django.urls import path

from .views import *

urlpatterns = [
    path("", index),
    path("profile/", profile),
    path("wall/", wall),
    path("heap/", heap),
    path("thread/", thread),
    path("goroutine/", thread),
    path("cmdline/", cmdline),
]

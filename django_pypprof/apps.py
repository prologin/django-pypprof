# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2022 Association Prologin <association@prologin.org>
# Copyright (c) 2022 Marc 'risson' Schmitt <marc.schmitt@prologin.org>

import mprofile
from django.apps import AppConfig
from django.conf import settings


class DjangoPypprofConfig(AppConfig):
    name = "django_pypprof"

    def ready(self):
        try:
            mprofile.start(
                sample_rate=getattr(settings, "PPROF_SAMPLE_RATE", 128 * 1024)
            )
        # The profiler is already started.
        except RuntimeError:
            pass

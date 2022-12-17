# -*- coding: utf-8 -*-
from django.conf import settings

DEFAULT_SETTINGS = {}

USER_SETTINGS = DEFAULT_SETTINGS | getattr(settings, 'TESTPKG_SETTINGS', {})
globals().update(USER_SETTINGS)

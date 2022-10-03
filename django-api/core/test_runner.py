from importlib import import_module

from django.conf import settings
from django.db import connections
from django.test.runner import DiscoverRunner


class CoreTestRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        """We set the TESTING setting to True. By default, it's on False."""
        super().setup_test_environment(**kwargs)
        settings.TESTING = True

    def setup_databases(self, **kwargs):
        """We set the database"""
        kwargs["aliases"] = connections
        r = super().setup_databases(**kwargs)
        self.load_fixtures()
        return r

    @classmethod
    def load_fixtures(cls):
        try:
            module = import_module(f"api.fixtures")
            getattr(module, "run_fixtures")()
        except ImportError:
            return

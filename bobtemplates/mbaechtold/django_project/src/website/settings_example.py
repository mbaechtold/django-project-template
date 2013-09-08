from website.config.common import BaseSettings
from website.config.mixins import DevMixin


class DevDefaultSite(DevMixin, BaseSettings):
    pass


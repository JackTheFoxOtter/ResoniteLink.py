"""
ResoniteLink.py
~~~~~~~~~~~~~~~

A python wrapper for the ResoniteLink API.
Resonite and ResoniteLink are Copyright (c) Yellow Dog Man Studios S.R.O

:copyright: (c) 2026-present JackTheFoxOtter
:license: MIT, see LICENSE for more details.

"""
__title__ = "ResoniteLink.py"
__author__ = "JackTheFoxOtter"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2026-present JackTheFoxOtter"
__version__ = "0.1.0b"
__path__ = __import__('pkgutil').extend_path(__path__, __name__)


# Logging setup is run first, otherwise we miss logging during import phase.
# NOTE: If you want to use your own logging configuration, simply configure it before importing this module,
#       setup_logging does nothing if the root logger already has handlers configured.
from .logging import setup_logging
setup_logging()

from .exceptions import *
from .types import *
from .json import *
from .math import *
from .models.assets.mesh import *
from .models.datamodel import *
from .models.messages import *
from .models.responses import *
from .proxies import *
from .utils import *
from .client import *

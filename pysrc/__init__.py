import os
import sys
from .http_client import HttpClient
from .rpc_interface import RPCInterface, WalletClient
from .chainapi_sync import ChainApi
from . import _pyflonkit

__version__='1.1.12'

_pyflonkit.init()

eosapi = ChainApi()

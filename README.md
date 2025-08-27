Python Toolkit for EOS

[![PyPi](https://img.shields.io/pypi/v/pyflonkit.svg)](https://pypi.org/project/pyflonkit)
[![PyPi](https://img.shields.io/pypi/dm/pyflonkit.svg)](https://pypi.org/project/pyflonkit)

# Installation

## On Linux platform

```bash
python3 -m pip install -U pip
python3 -m pip install pyflonkit
```

## On Windows platform:

```bash
python -m pip install -U pip
python -m pip install pyflonkit
```

## On Apple M1 hardware

pyflonkit does not have pre-built versions available for ARM chips. in order to build it from source code, you need to install `cmake`, `go`, `scikit-build`, `cython`.

```bash
brew install go
brew install cython
xcode-select --install
python3 -m pip install -U pip
python3 -m pip install cmake
python3 -m pip install scikit-build
python3 -m pip install pyflonkit
```

# Code Examples

## Example1
```python
import os
from pyflonkit import eosapi, wallet
#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

eosapi.set_node('https://eos.greymass.com')
info = eosapi.get_info()
print(info)
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
```

## Async Example
```python
import os
import asyncio
from pyflonkit import wallet
from pyflonkit.chainapi import ChainApiAsync

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

async def test():
    eosapi = ChainApiAsync('https://eos.greymass.com')
    info = await eosapi.get_info()
    print(info)
    args = {
        'from': 'test1',
        'to': 'test2',
        'quantity': '1.0000 EOS',
        'memo': 'hello,world'
    }
    r = await eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
    print(r)

asyncio.run(test())
```

## Sign With Ledger Hardware Wallet Example
```python
import os
from pyflonkit import eosapi
eosapi.set_node('https://eos.greymass.com')
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}

#indices is an array of ledger signing key indices
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'}, indices=[0])
```




# [Docs](https://github.com/fullon-labs/pyflonkit/tree/master/docs)

# Building from Source Code

### Installing Prerequisites

```
python3 -m pip install scikit-build
python3 -m pip install cython
```

For Windows platform

```
python -m pip install scikit-build
python -m pip install cython
```

1. Download and Install gcc compiler from [tdm-gcc](https://jmeubank.github.io/tdm-gcc)
2. Install Go compiler from [download](https://golang.org/doc/install#download)
3. Install cmake from [download](https://cmake.org/download)
4. Install python3 from [downloads](https://www.python.org/downloads/windows/)

Press Win+R to open Run Dialog, input the following command
```
cmd -k /path/to/gcc/mingwvars.bat
```

### Downloading Source Code

```
git clone https://github.com/fullon-labs/pyflonkit
cd pyflonkit
git submodule update --init --recursive
```

### Build
```
./build.sh
```

For Windows platform, in the cmd dialog, enter the following command:
```
python setup.py sdist bdist_wheel
```

### Installation

```
./install.sh
```

For Windows platform
```
python -m pip uninstall pyflonkit -y;python -m pip install .\dist\pyflonkit-[SUFFIX].whl
```

### License
[MIT](./LICENSE)

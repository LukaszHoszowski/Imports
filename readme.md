# Modules and packages

```python
import urllib
from urllib.request import urlopen
from urllib.request import urlopen as op
```

```python
if __name__ == '__main__':
    pass
```
__name__ - context

sys.path - sciezki w ktorych znajduja sie biblioteki pythona
'' - current folder

import sys
sys.path.append('test_example')
export PYTHONPATH='test_example'
$PYTHONPATH
sys.path
python -m elo

## PACKAGES
- 3.3+ '__init__' optional
- PEP420

import *  - nie importuje rzeczy z _ na poczatku
locals() - to check imported modules

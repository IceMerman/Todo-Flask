# TODO app (flask based)

## Compatibily issues

### To runt test
In order to test the application you need to edit the file located at **\Lib\site-packages\flask_testing\utils.py**
and edit those lines

Line 35:
```python
#from werkzeug import cached_property
from werkzeug.utils import cached_property
```

Line 304:
```python
# if parts.netloc:
if parts.path:
```
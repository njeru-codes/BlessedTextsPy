# blessedtexts-py


## installation
```bash
    pip install blessedtexts-py
```

## usage
```python
from blessedtexts_py import SmsAPI

sms_api = SmsAPI( "api_key", "sender_id")

sms_api.send_sms("711XXXXXXXX", message="new message")

```

## contributing
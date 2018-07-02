from ews_usage import get_ews_usage
import json

print(json.dumps(get_ews_usage(), indent=4))

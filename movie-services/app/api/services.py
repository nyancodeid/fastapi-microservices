import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/casts/'
url = os.environ.get('CAST_SERVICE_HOST_URL') or CAST_SERVICE_HOST_URL

def is_cast_present(cast_id: int):
  r = httpx.get(f'{url}{cast_id}')
  return True if r.status_code == 200 else False
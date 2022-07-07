import os
from transpose import Transpose

key = os.environ.get("TRANSPOSE_KEY")
api = Transpose(key)

# Can now pass the API in and call other atoms from here
from atoms.recent_token_transfers import recent_token_transfers
recent_token_transfers(api, "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", 10)
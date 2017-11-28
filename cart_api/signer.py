import os
from itsdangerous import Signer, URLSafeSerializer


SHARED_SECRET_TOKEN = os.getenv('SNAPCART_SHARED_SECRET_TOKEN', '|z3{XSkyLd3$7GkVa#d`IIZzl#`p=(N?IZ!jLO=^s4**cuD.[,{8q@+J7d:HT}p')
SIGNER = Signer(SHARED_SECRET_TOKEN)
URL_SAFE_SIGNER = URLSafeSerializer(SHARED_SECRET_TOKEN)
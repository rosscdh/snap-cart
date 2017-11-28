from signer import URL_SAFE_SIGNER


def sign_product(name: str, price: str):
    return URL_SAFE_SIGNER.dumps({'name': name, 'price': price})


def unsign_product(signature: str):
    return URL_SAFE_SIGNER.loads(signature)

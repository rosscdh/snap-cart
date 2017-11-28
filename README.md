# snap-cart

PoC for a really fast cart system


### Run

```
docker-compose up
```

### Use

```
cat fixtures/basic.json | http post http://127.0.0.1:8080/cart/my-cart-id
```

### Shared secret signature

To prevent the user from tampering with the product info and pricing, a shared secret is used to cryptographicaly encrypt the name and price

__Set your token__

```
export SNAPCART_SHARED_SECRET_TOKEN='somethign really complicated and long'
```

__Sign your products__

```
apistar sign_product 'name of product' 25.55
  eyJuYW1lIjoibmFtZSBvZiBwcm9kdWN0IiwicHJpY2UiOiIyNS41NSJ9.RpSTtPDsKNcYlqirhynYS57xTtg

apistar unsign_product 'eyJuYW1lIjoibmFtZSBvZiBwcm9kdWN0IiwicHJpY2UiOiIyNS41NSJ9.RpSTtPDsKNcYlqirhynYS57xTtg'
  {'name': 'name of product', 'price': '25.55'}
```
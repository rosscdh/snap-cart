# snap-cart

PoC for a really fast cart system

### Rationale

Carts at scale are very complicated.. and slow
Make a fast cart that cant handle many many requests without significant touching of the database
1. Validate that the user has not tampered with the sent data (without a db lookup on product)
2. Treat the cart as a statemachine: this implies sending the COMPLETE cart everytime something in the cart changes (yes, yes, higher data tx/rx but better less handling of state on the server-side)
3. Assume the client is always right, but validate they have not tampered with the important things (price,name)

### Run

```
docker-compose up
```

### Use

```
cat fixtures/basic.json | http post http://localhost:8080/cart/my-cart-id

cat fixtures/add_product.json | http post http://localhost:8080/cart/my-cart-id/products

cat fixtures/thin-cart.json | http post http://localhost:8080/cart/my-cart-id
cat fixtures/fat-cart.json | http post http://localhost:8080/cart/my-cart-id
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
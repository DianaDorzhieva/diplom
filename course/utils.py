import stripe
from config.settings import stripe_api_key


def create_product(payment):
    stripe.api_key = stripe_api_key
    product = stripe.Product.create(name=payment.name)

    product_price = stripe.Price.create(
        currency="rub",
        unit_amount=payment.price * 100,
        product_data={"name": product.get('name')}
    )

    product_url = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": product_price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return product_url['url']

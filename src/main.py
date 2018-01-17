from pubsub.rabbit import PubSub

# TODO: TemporaryException, PermanentException
# TODO: check blocking connection thing of rabbitmq

ps = PubSub()


@ps.listen('signup_completed.User')
def on_signup_completed(user):
    print('Send welcome email:', user.email)
    # ps.publish('email_sent', Email)


@ps.listen('order_placed.Order')
def on_order_placed(order):
    print(f'Order #{order.id} placed, pending payment')
    print('Send confirmation email:', order.customer.email)
    # ps.publish('email_sent', Email)


@ps.listen('order_canceled.Order')
def on_order_canceled(order):
    print(f'Order #{order.id} canceled')
    print('Send cancelation email:', order.customer.email)
    # ps.publish('email_sent', Email)


if __name__ == "__main__":
    print('Starting pubsub...')
    ps.run()

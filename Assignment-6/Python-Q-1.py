
orders = [
    {
        'id': 101,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'Ravi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'Meera',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]


def analyse(orders):

    revenue = {}
    products = {}
    customer_status = {}

    for order in orders:

        name = order['customer']
        status = order['status']

        # Store customer status
        if name not in customer_status:
            customer_status[name] = []

        customer_status[name].append(status)

        # Ignore cancelled orders
        if status == 'CANCELLED':
            continue

        total = 0

        # Calculate revenue and product quantity
        for item in order['items']:

            product = item[0]
            quantity = item[1]
            price = item[2]

            total += quantity * price

            products[product] = products.get(product, 0) + quantity

        revenue[name] = revenue.get(name, 0) + total

    # Find top 2 products
    top_products = sorted(
        products.items(),
        key=lambda x: (-x[1], x[0])
    )[:2]

    # Find fully delivered customers
    fully_delivered = []

    for name in customer_status:
        if all(status == 'DELIVERED'
               for status in customer_status[name]):
            fully_delivered.append(name)

    fully_delivered.sort()

    return {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }


result = analyse(orders)
print(result)

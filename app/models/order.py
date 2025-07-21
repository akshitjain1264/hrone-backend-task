def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "products": order["products"],  # list of {product_id, quantity}
    }

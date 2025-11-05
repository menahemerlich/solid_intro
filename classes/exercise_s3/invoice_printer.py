
class InvoicePrinter:
    @staticmethod
    def print_invoice(order):
        print(f"items: {order.items}, price: {order.total_price}")



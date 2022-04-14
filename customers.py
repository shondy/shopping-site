"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name} {self.last_name}, {self.email}, {self.password}>"
        )


def read_customers_from_file(filepath):
    """Read customer type data and populate dictionary of customer types.

    Dictionary will be {email: Customer object}
    """

    customer_types = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")

            customer_types[email] = Customer(
                first_name,
                last_name,
                email,
                password
            )

    return customer_types

def get_by_email(email):
    """Return a customer, given its email."""

    # This relies on access to the global dictionary `customer_types`

    return customer_types[email]

# Dictionary to hold types of customers.
#
# Format is {id: Customer object, ... }

customer_types = read_customers_from_file("customers.txt")

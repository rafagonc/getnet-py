import re


class CardNumber:
    card_number: str
    customer_id: str

    card_number_regex = re.compile(r"\A\d{13,19}\Z")

    def __init__(self, card_number: str, customer_id: str):
        if not self.card_number_regex.match(card_number):
            raise AttributeError(
                "Card Number is invalid, must contain only numbers and between 13 and 19 chars"
            )

        if len(customer_id) > 100:
            raise AttributeError("CustomerID must have bellow 100 characters.")

        self.card_number = card_number
        self.customer_id = customer_id

    def __str__(self):
        return self.card_number

    def __eq__(self, other):
        return (
            self.card_number == other.card_number
            and self.customer_id == other.customer_id
        )

    def as_dict(self) -> dict:
        return self.__dict__.copy()

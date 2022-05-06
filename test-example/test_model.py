from model import Batch, OrderLine
from datetime import date
# import pytest
# run from command line as "pytest test_model.py"


def test_allocating_to_a_batch_reduces_available_quanity():
    # inst a batch with a starting value of 20
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    # create an order of 2 units
    line = OrderLine('order-ref', "SMALL-TABLE", 2)

    batch.allocate(line)

    # check that the total quanity has been reduced from 20 to 18
    assert batch.available_quantity == 18

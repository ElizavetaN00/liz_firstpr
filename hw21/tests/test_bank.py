import pytest
from loguru import logger
from source.bank import Bank


@pytest.fixture
def bank():
    return Bank()


def test_register_client(bank):
    logger.info("Testing positive client registration")
    bank.register_client("0000001", "Elizaveta")
    assert "0000001" in bank.clients
    assert bank.clients["0000001"] == "Elizaveta"


def test_register_same_client(bank):
    logger.info("Testing registration with the same client id")
    bank.register_client("0000001", "Elizaveta")

    with pytest.raises(ValueError):
        bank.register_client("0000001", "Alvina")


def test_open_deposit_account(bank):
    logger.info("Testing positive deposit account opening")
    bank.register_client("0000001", "Elizaveta")
    bank.open_deposit_account("0000001", 1000, 1)
    assert "0000001" in bank.deposits
    assert bank.deposits["0000001"]["start_balance"] == 1000


def test_open_deposit_not_registered_client(bank):
    logger.info("Testing deposit opening for unregistered client")

    with pytest.raises(ValueError):
        bank.open_deposit_account("0000001", 1000, 1)


def test_open_same_deposit_multiple_times(bank):
    logger.info("Testing opening same deposit for same client")
    bank.register_client("0000001", "Elizaveta")
    bank.open_deposit_account("0000001", 1000, 1)

    with pytest.raises(ValueError, match="Deposit was already opened for this client"):
        bank.open_deposit_account("0000001", 2000, 2)

    assert bank.deposits["0000001"]["start_balance"] == 1000
    assert bank.deposits["0000001"]["years"] == 1


def test_calc_deposit_interest_rate(bank):
    logger.info("Testing deposit interest rate calculation")
    bank.register_client("0000001", "Elizaveta")
    bank.open_deposit_account("0000001", 1000, 1)
    final_balance = bank.calc_deposit_interest_rate("0000001")
    assert final_balance == 1104.713067441297


def test_calc_interest_no_opened_deposit(bank):
    logger.info("Testing interest calculation for client without deposit")
    client_id = "0000002"
    bank.register_client(client_id=client_id, name="No Deposit Client")

    with pytest.raises(ValueError) as e:
        bank.calc_deposit_interest_rate(client_id)

    assert str(e.value) == "No deposit found for this client"
    assert client_id not in bank.deposits


def test_close_deposit(bank):
    logger.info("Testing positive deposit closing")
    bank.register_client("0000001", "Elizaveta")
    bank.open_deposit_account("0000001", 1000, 1)
    bank.close_deposit("0000001")
    assert "0000001" not in bank.deposits


def test_close_deposit_no_client_opened(bank):
    logger.info("Testing closing nonexistent deposit")

    with pytest.raises(ValueError):
        bank.close_deposit("0000001")

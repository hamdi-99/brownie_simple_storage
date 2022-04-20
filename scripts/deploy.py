from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_sotrage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})

    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(30, {"from": account})
    transaction.wait(1)
    print(f"new value {simple_storage.retrieve()}")
    print(transaction)


def main():
    deploy_simple_sotrage()

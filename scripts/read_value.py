from brownie import SimpleStorage, config, accounts


def read_contract():
    simple_storage = SimpleStorage[-1]
    # to read we need abhi and bytecode of the contract
    simple_storage.retrieve()
    print(simple_storage.retrieve())


def main():
    read_contract()

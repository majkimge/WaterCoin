from brownie import accounts, H2OToken
from scripts.helpful_scripts import get_account


def createTokenTransfer():
    token = H2OToken[-1]
    account = get_account()
    balance = token.balanceOf(account)
    print(f"Balance of acc1: {token.balanceOf(account)}")
    account2 = "0xc2f1FB4e03b5850E356B2D30266821f2B5745478"
    print(f"Balance of acc2: {token.balanceOf(account2)}")
    print("Sending to acc2")
    tx = token.transfer(account2, 10 ** 20, {"from": account})
    tx.wait(1)
    print(f"Balance of acc1: {token.balanceOf(account)}")
    print(f"Balance of acc2: {token.balanceOf(account2)}")


def createToken():
    account = get_account()
    return H2OToken.deploy(10 ** 24, {"from": account})


def transact():
    token = None
    account = get_account()
    if len(H2OToken):
        token = H2OToken[-1]
    else:
        token = createToken()
    print(token)


def main():
    createTokenTransfer()

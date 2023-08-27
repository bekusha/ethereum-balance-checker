from django.shortcuts import render
from django.http import JsonResponse
from web3 import Web3


def index(request):
    return render(request, './templates/index.html')


def ethereum_balance(request, address):
    # Connect to an Ethereum node (replace with your own node URL)
    w3 = Web3(Web3.HTTPProvider(
        'HTTP://127.0.0.1:7545'))

    if w3.is_connected():
        try:
            balance_wei = w3.eth.get_balance(address)
            balance_eth = w3.from_wei(balance_wei, 'ether')
            response_data = {
                'address': address,
                'balance_wei': balance_wei,
                'balance_eth': balance_eth
            }
            print("This is balance: ", response_data)
            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({'error': 'Error fetching balance'})
    else:
        return JsonResponse({'error': 'Failed to connect to Ethereum node'})

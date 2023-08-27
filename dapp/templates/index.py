from web3 import Web3
from django.http import JsonResponse


def ethereum_balance(request, address):
    # connect to a Ethereum node
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    address = '0x0b595aF1877550D35c0D4C3F4F955F94d4009CF2'

    if w3.is_connected():
        try:
            balance_wei = w3.eth.get_balance(address)
            balance_eth = w3.from_wei(balance_wei, 'ether')
            response_data = {
                'address': address,
                'balance_wei': balance_wei,
                "balance_eth": balance_eth
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': 'Error fetching balance...'})
    else:
        return JsonResponse({'error': 'Failed to connect to Ethereum'})

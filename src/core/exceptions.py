'''
Тут содержатся всевозможные ошибки и исключения
'''

class UserNotFoundException(Exception):
    pass

class UserAlreadyExistException(Exception):
    pass

class PrizesUserNotFoundException(Exception):
    pass

class NftsUserNotFoundException(Exception):
    pass

class NftUserNotFoundException(Exception):
    pass

class NftNotFoundException(Exception):
    pass

class NftAlreadyExistException(Exception):
    pass

class PrizeNotFoundException(Exception):
    pass

class PrizeAlreadyExistException(Exception):
    pass

class MarketNotFoundException(Exception):
    pass

class MarketAlreadyExistException(Exception):
    pass
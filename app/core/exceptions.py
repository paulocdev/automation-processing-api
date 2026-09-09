class DomainException(Exception):
    ## Exceção base para todas as regras de negócio ##

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InvalidDocumentTypeError(DomainException):
    ## Lançada quando um tipo de documento nao suportado é enviado ##

    pass

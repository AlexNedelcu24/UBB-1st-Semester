class Exception(Exception):
    pass

class ValidationException(Exception):
    def __init__(self, mes):
        """
        :param mes: lista de erori
        """
        self.__error_mes = mes

    def getMes(self):
        return self.__error_mes

    def __str__(self):
        return 'Validation Exception: ' + str(self.__error_mes)


class RepositoryException(Exception):
    def __init__(self, mes):
        self.__mes = mes

    def getMessage(self):
        return self.__mes

    def __str__(self):
        return 'Repository Exception: ' + str(self.__mes)


class DuplicateIDException_Book(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Exista deja o carte cu id-ul dat.")


class BookNotFoundExcetion(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nu exista o carte cu acest id")


class DuplicateIDException_Client(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Exista deja un client cu id-ul dat.")


class ClientNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nu exista un client cu acest id")





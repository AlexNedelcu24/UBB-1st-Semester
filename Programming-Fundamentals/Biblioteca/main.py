from Domain.validators import BookValidator
from Domain.validators import ClientValidator
from Repository.book_repo import InMemoryRepository_Book
from Repository.client_repo import InMemoryRepository_Client
from Repository.loan_repo import InMemoryRepository_Loan
from service.book_service import BookService
from service.client_service import ClientService
from service.loan_service import LoanService
from ui.console import Console

val1 = BookValidator()
val2 = ClientValidator()
repo1 = InMemoryRepository_Book('F:\\FP\\Biblioteca\\data\\books.txt')
repo2 = InMemoryRepository_Client('F:\\FP\\Biblioteca\\data\\clients.txt')
repo3 = InMemoryRepository_Loan()
srv1 = BookService(repo1, val1)
srv2 = ClientService(repo2, val2)
srv3 = LoanService(repo3)
ui = Console(srv1, srv2, srv3)
ui.command_ui()

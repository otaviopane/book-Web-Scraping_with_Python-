from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
    # devolve null, executa um break ou algum outro "Plano B"
else:
    # o programa continua. Nota: se você retornar ou executar um break no
    # catch da exceção, não será necessário usar a instrução "else"
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.html)
    print('It worked!')

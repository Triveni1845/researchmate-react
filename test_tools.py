from tools import calculate,search_documents
from dispatcher import dispatch
def test_calculator(): assert calculate(0.12,250)['result']==30
def test_search(): assert search_documents('internship')['matches']
def test_unknown_tool(): assert dispatch('delete_all',{})['error']=='not_allowed'
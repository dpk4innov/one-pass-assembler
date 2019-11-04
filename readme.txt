output when errors are present->

deepak@deepak-HP-Pavilion-15-Notebook-PC:~$ python3 assembler.py
symbol table:
['a', 'd', 0, 4, 2, 'D']
['p', 'd', 8, 1, 18, 'D']
['c', 'd', 26, 1, 15, 'D']
['e', 'b', 0, 1, 1, 'D']
['printf', 't', '', '', '', 'U']
['abc', 't', '', '', '', 'U']
['main', 't', '', '', '', 'U']
['abc', 't', '', '', '', 'U']
error table:
[7, 'a', 1]
[13, '', 3]
[14, 'g', 4]
[16, 'l', 4]
line:7 error:'a'symbol redefined
line:13 error:invalid combination of opcode and operands
line:14 error:'g' error: symbol undefined
line:16 error:'l' error: symbol undefined

output when errors are  not present->

deepak@deepak-HP-Pavilion-15-Notebook-PC:~$ python3 assembler.py
symbol table:
['a', 'd', 0, 4, 2, 'D']
['p', 'd', 8, 1, 18, 'D']
['c', 'd', 26, 1, 15, 'D']
['e', 'b', 0, 1, 1, 'D']
['q', 'b', 0, 4, 8, 'D']
['printf', 't', '', '', '', 'U']
['abc', 't', '', '', '', 'U']
['main', 't', '', '', '', 'U']
['abc', 't', '', '', '', 'U']
error table:


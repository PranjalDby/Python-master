from pprint import pprint

# hence parser module is removed and deprecated: I create a env python 3.9'
import parser
import symbol
import token
# st = parser.expr('a + 1')
# pprint(parser.st2list(st))

def lex(expreesion):
    symbols = {v:k for k,v in symbol.__dict__.items() if isinstance(v,int)}
    tokens= {v:k for k,v in token.__dict__.items() if isinstance(v,int)}
    lexicon = {**symbols,**tokens}
    st = parser.expr(expreesion)
    st_list = parser.st2list(st)
    pprint(lexicon)
    def replace(l:list):
        r = []
        for i in l:
            if isinstance(i,list):
                r.append(replace(i))
            
            else:
                if i in lexicon:
                    r.append(lexicon[i])
                else:
                    r.append(i)

        return r
    
    return replace(st_list)


pprint(lex('3*a + 2*b'))

import instaviz
def example():
    a = 1
    b = a + 1 * 2
    return b
instaviz.show(example)
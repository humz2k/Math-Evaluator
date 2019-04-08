class Parser:
    def __init__(self):
        self.trees = {}
        self.available_symbols = [i for i in "() 0123456789+-*/^%!"]
        
    def parse(self,statement):
        assert not any(not i in self.available_symbols for i in statement), f"Statement must only contain these symbols: {self.available_symbols}"

        statement = [list(i) for i in statement if not i == " "]
        counter = 0
        tree = []

        while counter < len(statement):
            if statement[counter] == ["("]:
                expr = []
                while counter < len(statement): 
                    counter += 1
                    if statement[counter] == ["("]:
                        chunk,counter = self._de_layer(statement,counter)
                        expr.append(chunk)
                    elif not statement[counter] == [")"]:
                        expr.append(statement[counter])
                    else:
                        break
                if len(expr):
                    tree.append(expr)
                expr = []
            elif not statement[counter] == [")"]:
                tree.append(statement[counter])
            counter += 1

        self.trees[len(self.trees.keys())] = self._join(tree)

    def _join(self,tree):
        total = []
        for i in tree:
            if isinstance(i[0],list):
                total.append(self._join(i))
            else:
                total.append(*i)
        return total
                
    def _de_layer(self,statement,counter):
        new = []
        while counter < len(statement)-1:
            if statement[counter] == ["("]:
                tmp,counter = self._de_layer(statement,counter+1)
                new.append(tmp)
            if statement[counter] == [")"]:
                return new,counter
            new.append(statement[counter])
            counter += 1

    def show(self,tree=None):#add validation check
        if tree is None or not isinstance(tree,int) or tree >= len(self.trees.keys()):
            for k,v in self.trees.items():
                print(f"Tree {k}: {v}")
        else:
            print(f"Tree {tree}: {self.trees[tree]}")

    def request(self,index):
        assert isinstance(index,int) and index < len(self.trees), "Enter valid integer"
        return self.trees[index]

class Evaluator:
    def __init__(self):
        self.answers = {}

    def eval(self,parsetree):
        for term in parsetree:
            if isinstance(term,list):
                term = self.eval(term)

    def show(self,ans=None):
        pass

a = "( 1 + 1 ) - ( 2 *-22 /(2 - (2**2)))"
#[['1', '+', '1'], '-', ['2', '*', '-', '2', '2', '/', [['2', '-', ['2', '*', '*', '2']]]]]

#b = "2+2*2*2"
#add variables e.g x*(2 + x) parses to x**2 + 2x
parser = Parser()
evaluator = Evaluator()

parser.parse(a)
parser.show()
parsed_a = parser.request(0)
evaluator.eval(parsed_a)
evaluator.show()


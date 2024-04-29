import LRLib

grammar = {
    'expression':["expression plus term",'term'],
    'term':["term times factor",'factor'],
    'factor':["lparen expression rparen","id"]
}

grammar = LRLib.augment_grammar(grammar)
# simbolo = next(iter(grammar))

# res = LRLib.closure({(simbolo,tuple(grammar[simbolo][0].split(' ')),0)},grammar)
# for item in res:
#     print(LRLib.represent_item(item))

# res = LRLib.goto({('E`',('E',),1),('E',('E','+','T'),1)},'+',grammar)

# for item in res:
#     print(LRLib.represent_item(item))

automata = LRLib.generate_LRAutomata(grammar)
automata_graph = LRLib.plot_af(automata.start)
nombre_archivo_pdf = 'Automata LR'
automata_graph.view(filename=nombre_archivo_pdf,cleanup=True)
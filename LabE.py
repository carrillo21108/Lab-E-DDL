import LRLib
import pickle

#Lectura del objeto pkl
with open('grammar.pkl', 'rb') as archivo_entrada:
    grammar = pickle.load(archivo_entrada)

grammar = LRLib.augment_grammar(grammar)

automata = LRLib.generate_LRAutomata(grammar)
automata_graph = LRLib.plot_af(automata.start)
nombre_archivo_pdf = 'Automata LR'
automata_graph.view(filename=nombre_archivo_pdf,cleanup=True)
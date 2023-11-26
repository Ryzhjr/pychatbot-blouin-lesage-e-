def fct_ponct1(a):
    p1='!()[]{};:"\,<>./?@#$%^&*_~'
    new_a=''
    for caracteres in a:
        if caracteres not in p1:
            new_a+= caracteres
    return(new_a)
def fct_ponct2(a):
    p2="'-"
    new_a=''
    for caracteres in a:
        if caracteres in p2:
            new_a+= ' '
        else:
            new_a+= caracteres
    return(new_a)
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension): files_names.append(filename)
    return files_names
def fct_prenom_nom(l):
    dico_nom = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel',
                'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
    L=[]
    for cle in dico_nom.keys():
        for nom_fichier in l:
            if cle in nom_fichier:
                L.append(dico_nom[cle]+' '+cle)
    new_L=[L[0]]
    for i in range(1,len(L)):
        if L[i-1]!=L[i]:
            new_L.append(L[i])
    return(new_L)

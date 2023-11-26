from functions import *
if __name__=='__main__':
    directory = "./test"
    files_names = list_of_files(directory, "txt")
    nb_fichier=fct_nbfichier(files_names)
    liste_fichier=[]
    liste_dico=[]
    for i in range(len(files_names)):
        fichier=directory+'/'+files_names[i]
        with open(fichier,'r') as nb_fichier[i]:
            l=nb_fichier[i].read()
            liste_fichier.append(fct_ponct1(fct_ponct2(fct_minuscule(l))))
            liste_dico.append(fct_compteurmot1(fct_ponct1(fct_ponct2(fct_minuscule(l)))))
    fct_affichage(liste_fichier)

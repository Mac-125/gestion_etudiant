from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("etudiant.db")
    except:
        print("pas d'accès")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not etudiant_nom.get():
        t1.insert(END,"<> le nom de l'étudiant est requis <>\n")
        a=1
    if not numero_id.get():
        t1.insert(END,"<>le numero id est requis <>\n")
        b=1
    if not branche.get():
        t1.insert(END,"<> la brache est requise <>\n")
        c=1
    if not telephone.get():
        t1.insert(END,"<>le numero de téléphone est requis <>\n")
        d=1
    if not nom_pere.get():
        t1.insert(END,"<>le nom du père est requis <>\n")
        e=1
    if not adresse.get():
        t1.insert(END,"<>l'adresse est Requise <>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def ajouter():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS ETUDIANTS(NOM TEXT,NUMERO_ID INTEGER,BRANCHE TEXT,TELEPHONE_NO INTEGER,NOM_PERE TEXT,ADRESSE TEXT)")
                cur.execute("insert into ETUDIANTS values(?,?,?,?,?,?)",(etudiant_nom.get(),int(numero_id.get()),branche.get(),int(telephone.get()),nom_pere.get(),adresse.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"L'ETUDIANT A ETE AJOUTE \n")


def voir():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from ETUDIANTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def supprimer():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM ETUDIANTS WHERE NUMERO_ID=?",(int(numero_id.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"L'ETUDIANT A ETE SUPPRIME\n")

def mettre_a_jour():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE ETUDIANTS SET NOM=?,NUMERO_ID=?,BRANCHE=?,TELEPHONE=?,NOM_PERE=?,ADRESSE=? where NUMERO_ID=?",(etudiant_nom.get(),int(numero_id.get()),branche.get(),int(telephone.get()),nom_pere.get(),adresse.get(),int(numero_id.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"MISE A JOUR REUSSIE\n")


def fermer():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("gestion d'étudiants")
     
    etudiant_nom=StringVar()
    numero_id=StringVar()
    branche=StringVar()
    telephone=StringVar()
    nom_pere=StringVar()
    adresse=StringVar()
    
    label1=Label(root,text="NOM:")
    label1.place(x=0,y=0)

    label2=Label(root,text="NUMERO_ID:")
    label2.place(x=0,y=30)

    label3=Label(root,text="BRANCHE:")
    label3.place(x=0,y=60)

    label4=Label(root,text="TELEPHONE:")
    label4.place(x=0,y=90)

    label5=Label(root,text="NOM DU PERE:")
    label5.place(x=0,y=120)

    label6=Label(root,text="ADRESSE:")
    label6.place(x=0,y=150)

    e1=Entry(root,textvariable=etudiant_nom)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=numero_id)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=branche)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=telephone)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=nom_pere)
    e5.place(x=100,y=120)

    e6=Entry(root,textvariable=adresse)
    e6.place(x=100,y=150)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="AJOUTER UN ETUDIANT",command=ajouter,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VOIR TOUS LES ETUDIANTS",command=voir,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="SUPPRIMER UN ETUDIANT",command=supprimer,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="METTRE A JOUR LES INFORMATION",command=mettre_a_jour,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="FERMER",command=fermer,width=40)
    b5.grid(row=15,column=0)


    root.mainloop()

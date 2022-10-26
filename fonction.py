

def lireFichier():
    fileRead = open('admissions.txt','r')
    lines = fileRead.readlines()
    print(lines)
    fileRead.close()

def creerTable():
    fileWrite = open('creation_admissions.sql','w')
    fileWrite.write('CREATE TABLE Profil(etudiant_id INT NOT NULL, score_GRE NUMERIC(3,0), score_TOEFL NUMERIC(3,0),university_rating INTEGER,SOP FLOAT,ML FLOAT, CGPA FLOAT, research BOOLEAN NOT NULL, admission BOOLEAN NOT NULL);')
    fileWrite.close()

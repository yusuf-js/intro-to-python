#case check nilai siswa

#if
#format
#if kondisi :
#   apa yang dilakukan kalau kondisi terpenuhi
try:
    nilai = 90
    if nilai > 80 or nilai <89:
            print("siswa ini lulus")
    else:  
            print("siswa ini bodoh")
except: 
       print("siswa ini tidak lulus")



pesan = "siswa jago cok" if nilai > 80 else "siswa ieu belegug"    
print(f"{pesan}")

if nilai > 80:
       print("Nilai anda lulus sempurna")
elif nilai >= 70 and nilai < 80 :
       print("sedikit lagi kamu tidak lulus")
else :
       print("kamu tidak lulus")


#kasus untuk menu
#match and case
print("2. start")
print("2. exit")
selection = input ("selection >>")
match selection :
       case "1":
              print("start game")
       case "2":
              print("exit")
       case _ :
              print("input not valid")      
#just a normal calculator but without trigonometry and square root

print("==Kalkulator==")
print("==Silahkan Gunakan dan/atau tanda tanda operasi matematika berikut ini==")
print("== Tambah ( + ) | Kurang ( - ) | Kali ( * ) | Bagi ( / ) == ")
print("==Format: 1+1 | 1/1 ==") #Format

while True : #Pengulangan
 try :
  Hitung = eval(input(" ")) #penghitungan 
  print("= " + str( Hitung)) #hasil
 except ZeroDivisionError :
  print("Error")
 except Exception :
  print("Error Format")

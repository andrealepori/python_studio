#print("Hello, World!");
#print("sono il barista!");

#drink_speciale="DigitalVodka"
#print(drink_speciale);
#drink_speciale="senzaVodka"
#print(drink_speciale);


#nome="Luca";
#eta=28;
#anno_nascita=1995;
#ruolo="barman"
#pub_aperto=False;
#print(nome);
#print(eta);
#print(ruolo);
#print(pub_aperto);

#print("Assaggia")
#print(drink_speciale)


#stringa_utente=input()
#print (stringa_utente)
#print("come ti chiami?")
#nome_cliente=input()
#print( "benvenuto")
#print(nome_cliente)
#print( "in che anno sei nato?")
#anno_nascita = input()
#print("sei nato nel:")
#print(anno_nascita)

#print("hai a disposizione")
#drink_disponibili = 5+5
#print(drink_disponibili) 
"""
drink_disponibili = 5

drink_disponibili = 5-2
print(drink_disponibili)
prezzo_drink= 3.45;

print (drink_disponibili- prezzo_drink)

#Imparare a programmare da zero. Corso di Programmazione Python per Principianti Tutorial Python ITA 23:20

#operatori stringa

nome_barman="edoBot";

nome_barman2="ugoBot";
print (nome_barman +  nome_barman2);


a = 3;
b = "123";

c= a + int(b);
print (c);

print("inserisci il tuo anno");
anno_nascita = int(input())
anni_cliente = 2021 - anno_nascita;
print( "Hai"+ str(anni_cliente)+ "anni")

if anni_cliente < 18:
  print("sei maggiorenne") 
else:
   print("sei minorenne") 
"""




a = 13
b = 23
c = 33
d = 43 
e = 23 

if a > b:
  print("a = b")
else:
  print("a diverso da b")

if a > b:
  print( "a è maggiore di b")
else:
    print("b è maggiore di A")



if a == b:
  print('siamo uguali')
else:
  print('siamo diversi');

if e > c == a:
  print ("e > c > a")
else:
   print ("e < c < a")


ma = 20
me = 20
mi = 20

if ma == mi:
  print( "siamo uguali")
else:
  print("siamo diversi")

if ma == mi == me:
  print( "siamo BELLI")
else:
  print("siamo BRUTTI")
  
print (ma + me + mi)
print (ma + me - mi)
print (ma / me + mi)
print (ma * me - mi)


prezzo_drink = 5.50
sconto = 1
cliente_preferito = 'luca'

if cliente_preferito == 'luca':
  print ("tu bevi")
else:
  print ("tu non bevi")


prezzo_drink = 5.50
sconto = 1

cliente_preferito = 'luca'
print("come ti chiami?")
nome_cliente = input()
print("quanti anni hai?")
anni_cliente = int(input())    
if nome_cliente==cliente_preferito and anni_cliente>18:
   prezzo_drink==sconto
print("il prezzo del drink è"+str(prezzo_drink))



alcolici = ["vodka", "rhum",]
print(alcolici)

alcolici = ["1"]
alcolici.append("ARMAGNAC")
print(alcolici)

alcolici.append("CHACACA")
print(alcolici)

alcolici.append("CALVADOS")
print(alcolici)

alcolici.insert(0, "CHAMPAGNE")
print(alcolici)
alcolici.remove( "CHACACA")
print(alcolici)
alcolici[1] ="MAGNUM"
print(alcolici)
import time

print("Esse game está sendo desenvolvido por apenas if e else em python espero que gosta do game base")
time.sleep(1)


pontuacao=0

time.sleep(2)
print("")
print("1 - Qual game esta sendo desenvolvido pela rockstar esse ano")
print("")
print("1- GTA V")
print("2- Gta San Andres ")
print("3 - Red Ded Company")
print("4- GTA VI")

time.sleep(2)

jogar = input (">>>")

if jogar == "4" :
    print("Resposta correta")
    pontuacao =  +1
else :
    print("Resposta incorreta")



time.sleep(2)
print("")
print("2 - Quais games foram desenvolvido pela rockstar ")
print("")
print("1- GTA V , Midnight , Red dead redemption, bully, maxPayne")
print("2- Bomba Path, Fifa , Pes, Dream Ligue Soccer ")
print("3 - Call of duty, DayLight, The walking dead")
print("4- Nenhuma das opções")
time.sleep(2)

jogar = input (">>>")

if jogar == "1" :
    print("Resposta correta")
    pontuacao =  +1
else :
    print("Resposta incorreta")
    
time.sleep(2)

time.sleep(2)
print("")
print("3 - Qual empresa a Actiovision foi comprada ")
print("")
print("1- Appe")
print("2- Microsoft ")
print("3 - Linux")
print("4- Nenhuma das opções")
time.sleep(2)

jogar = input (">>>")

if jogar == "2" :
    print("Resposta correta")
    pontuacao =  +1
else :
    print("Resposta incorreta")
    
time.sleep(2)


time.sleep(2)
print("")
print("4 - Qual game foi mais jogado durante a pandemia de 2021 ")
print("")
print("1- GTA V , Red dead redemption")
print("2- Fifa , Pes ")
print("3 - Call of duty, DayLight, The walking dead")
print("4- Nenhuma das opções")
time.sleep(2)

jogar = input (">>>")

if jogar == "1" or jogar == "2" or jogar =="3":
    print("Resposta correta")
    pontuacao =  +1
else :
    print("Resposta incorreta")
    
time.sleep(2)


print("")
print("Você fez no total : ",jogar)
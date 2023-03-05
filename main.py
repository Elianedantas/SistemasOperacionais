import logging, threading, time, random

colocacao = list()

def thread_function(name):
  p = " "
  soma_pulos = 0
  qtd_pulos = 0
  while (soma_pulos < 21):
    pulos = random.randint(1, 3)
    if((pulos >= 1 ) and (pulos <= 3)):
      soma_pulos += pulos
    qtd_pulos += 1
    p += " ► "
    print(name, p, "(Pulo em metros:", pulos, "- Distância percorrida:", soma_pulos, " metros).\n")
    if (soma_pulos >= 20):
      print(name, " ganhou com ", qtd_pulos, " pulos!\n")
      colocacao.append(name)
      return
    time.sleep(2)

if __name__ == "__main__":
  threads = list()
  print("*---------------------------*")
  print("****** FAÇA SUA APOSTA ******")
  print("* 1 para apostar na Lebre 1 *")
  print("* 2 para apostar na Lebre 2 *")
  print("* 3 para apostar na Lebre 3 *")
  print("* 4 para apostar na Lebre 4 *")
  print("* 5 para apostar na Lebre 5 *")
  opcao = int(input("\t\t  Opção: "))
  print("*---------------------------*\n\n")
  for c in range(5):
    x = threading.Thread(target=thread_function, args=(f"Lebre {c+1}",))
    threads.append(x)
    x.start()

  for thread in threads:
    thread.join()
  teste = colocacao[0]
  print("\n\n*----------------------*")
  print("*** ORDEM DE CHEGADA ***")
  for index, lebre in enumerate(colocacao):
    print(f"* {index+1}º colocado: {lebre} *")
    if(index == 0):
      teste = lebre[6:]
  print("*----------------------*")
  print("*----- RESULTADO: -----*")
  if (opcao == int(teste)):
    print("     VOCÊ GANHOU :)     ")
  else:
    print("     VOCÊ PERDEU :(     ")
  print("*----------------------*")
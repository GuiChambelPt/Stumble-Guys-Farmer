import cv2
import pyautogui as pudim
vezes = input('Quantas vezes queres rodar o progama:')
vezesexecutado = 0
vezesexecutado = int(vezesexecutado)
vezes = int(vezes)
parar = False
def inicial():
    global vezesexecutado
    global vezes
    global parar
    while True:
        if vezesexecutado == vezes:
                parar = True
                print('fixe')
                conta = vezesexecutado * 20
                print('Foram ganhas {} estrelas e o progama foi executado {} vezes'.format(conta, vezesexecutado))
                quit()
        else:
            global menuinicial
            global jornal
            menuinicial = True
            while menuinicial == True:
                jornal = pudim.locateOnScreen('./images/portuguese/inicial.png', confidence=.7)
                if jornal ==  None:
                    print('Not found')
                else:
                    print('Found')
                    menuinicial = False
                    global jogar
                    jogar = True
                    while jogar == True:
                        playbutton = pudim.locateOnScreen('./images/portuguese/play.png', confidence=.7)
                        if playbutton ==  None:
                            print('Not found')
                            print(playbutton)
                        else:
                            print('playbutton')
                            pudim.moveTo(playbutton, duration=.1)
                            pudim.click(interval=.3)
                            print('Found')
                            jogar = False
                            global sair
                            sair = True
                            while sair == True:
                                leavebutton = pudim.locateOnScreen('./images/portuguese/leave.png', confidence=.7)
                                if leavebutton ==  None:
                                    print('Not found')
                                else:
                                    pudim.moveTo(leavebutton, duration=.1)
                                    pudim.click(interval=.3)
                                    print('Found')
                                    sair = False
                                    global test
                                    global get1
                                    global restart
                                    get1 = True
                                    while get1 == True:
                                        getbutton = pudim.locateOnScreen('./images/portuguese/get.png', confidence=.7)
                                        if getbutton ==  None:
                                            print('Not found')
                                        else:
                                            pudim.moveTo(getbutton, duration=.1)
                                            pudim.click(interval=.3)
                                            print('Found')
                                            get1 = False
                                            vezesexecutado = vezesexecutado + 1
                                            print(vezesexecutado)
                                            conta = vezesexecutado * 20
                                            print('Foram ganhas {} estrelas e o progama foi executado {} vezes'.format(conta, vezesexecutado))

    

inicial()
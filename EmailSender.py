import smtplib

while 1:
        
                                print ('''

             
                              ______                 _ _    _____                _            
                             |  ____|               (_) |  / ____|              | |           
                             | |__   _ __ ___   __ _ _| | | (___   ___ _ __   __| | ___ _ __  
                             |  __| | '_ ` _ \ / _` | | |  \___ \ / _ \ '_ \ / _` |/ _ \ '__| 
                             | |____| | | | | | (_| | | |  ____) |  __/ | | | (_| |  __/ |    
                             |______|_| |_| |_|\__,_|_|_| |_____/ \___|_| |_|\__,_|\___|_|    
                                                                          
                                                                                           
                                                                          
                                                                                            Developed By Jamaicah

                                      ''')

                              
                                messaggio = input('''Inserisci il tuo messaggio (non usare accenti) ->  ''')
                                host = input('Inserisci ip  del host -> ')
                                username = input ('Inserisci la tua email -> ')
                                password = input('Inserisci la tua password -> ')
                                destinatario = input('Inserisci il destinatario -> ')
                                porta = 587

                                email = smtplib.SMTP (host,porta)  #Inserimento porta e server
                                email.ehlo()  #richiesta connessione al server
                                email.starttls()  #connessione sicura la server
                                email.login(username,password)  #richiesta di login al server

                                email.sendmail(username,destinatario,messaggio)  #invio email
                                

                               

                                print ('''

                              ______                 _ _   _____            _       _        
                             |  ____|               (_) | |_   _|          (_)     | |       
                             | |__   _ __ ___   __ _ _| |   | |  _ ____   ___  __ _| |_ __ _ 
                             |  __| | '_ ` _ \ / _` | | |   | | | '_ \ \ / / |/ _` | __/ _` |
                             | |____| | | | | | (_| | | |  _| |_| | | \ V /| | (_| | || (_| |
                             |______|_| |_| |_|\__,_|_|_| |_____|_| |_|\_/ |_|\__,_|\__\__,_|
                             
                                                                                             Developed By Jamaicah
                                                                                            
                                  ''')


                                continuare = input('Vuoi riusare lo script? Si o No? ')

                                if continuare == "Si" or "si": 
                                    continue
                                elif continuare == "No" or "no":
                                    break
                                else:
                                    break


    
       




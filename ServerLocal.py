import socket
import DisorderCategories
from DisorderCategories import agent
import RulesDefiner


def server_program():
    # get the hostname
    # host = '172.105.155.108'
    host = 'localhost'
    port = 5001  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    while True:
        # configure how many client the server can listen simultaneously
        server_socket.listen(5)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        maxArr = []
        while True:
            data = conn.recv(4096).decode()
            if not data:
                # if data is not received break
                break
            print("name from connected user: " + str(data))
            name = str(data)
            DisorderCategories.reset_disorder_globals()
            RulesDefiner.resetglobals()
            user, rulesdict = DisorderCategories.main(name)
            if len(user.remaining_rules) == 1:
                baserule = user.remaining_rules.pop()
                for rule in baserule:
                    data = rule.get_query()
                    data += DisorderCategories.getResponseInputType(rule)
                    conn.send(data.encode())  # send data to the client
                    data = conn.recv(4096).decode()
                    if data == "stop":
                        path = user.name + ".p"
                        RulesDefiner.save_object(user, path)
                        break
                    checkbase(baserule, data, conn, user)
                if len(user.remaining_rules) == 0:
                    print("No more rules left")
                    maxArr = RulesDefiner.find_max_all_categories(DisorderCategories.flattendict(rulesdict))
                    print("Max array is : ", maxArr)
                    user.remaining_rules.extend(DisorderCategories.flattendict(rulesdict))
                    print(len(user.remaining_rules))
                    getfromAllRules(user, user.remaining_rules, conn, maxArr)
            else:
                maxArr = RulesDefiner.find_max_all_categories(DisorderCategories.flattendict(rulesdict))
                print("Max array is : ", maxArr)
                getfromAllRules(user, user.remaining_rules, conn, maxArr)

        conn.close()  # close the connection


def print_empathic_statements(user, conn):
    if len(user.reasons.keys()) > 0:
        data = ""
        for keyindex in user.reasons.keys():
            if keyindex == 0:
                data += "\nI like you just the way you are, hang in there." + "\n"
            if keyindex == 1:
                data += "Even if I am unable to understand exactly how you feel, I care about you and I wish to help" + "\n"
            if keyindex == 2:
                data += "You are fine just the way you are, don't go changing to try to please others\n"
            if keyindex == 3:
                data += "Things may seem hard, but they will get better, never stop fighting, I am here for you\n"
            if keyindex == 4:
                data += "You are not alone in this world, see, even today, you made a new friend - me."
            if keyindex == 5:
                data += "No matter how hard it gets, remember, you are the one in control\n. Dont push yourself to achieve standards set by others, Find your own path, I will support you along the way.\n"
        conn.send(data.encode())


def getfromAllRules(user, remainingrules, conn, maxvals):
    iterations = 1
    while len(remainingrules) > 0:
        print(iterations, "Is the current iteration")
        temprule = remainingrules.pop()
        data = temprule.get_query()
        data += DisorderCategories.getResponseInputType(temprule)
        tempindex = temprule.expectedtype
        conn.send(data.encode())
        data = conn.recv(8192).decode()
        if data == "stop":
            path = user.name + ".p"
            remainingrules.insert(0, temprule)
            RulesDefiner.save_object(user, path)
            break
        user = checkallCase(data, user, conn, tempindex, temprule)
        iterations += 1
    if len(maxvals) == 6:
        user.checkval(maxvals)
    print_empathic_statements(user, conn)
    data = "\nThanks for chatting with me today, it really made my day. Hope to see you soon.\n"
    conn.send(data.encode())
    path = user.name + ".p"
    RulesDefiner.save_object(user, path)
    return user


def getoncemore(inputrule, stringtoget, connection):
    stringtoget = stringtoget + "\n" + inputrule
    connection.send(stringtoget.encode())
    data = connection.recv(8192).decode()
    return data


def checkallCase(clientInput, user, conn, input_index, rule):
    if input_index == 1:
        if clientInput == "yes" or clientInput == "no" or clientInput == "stop":
            print("\nProcessing Input")
            if clientInput == "yes":
                user.setcategoryvals(rule.get_category_dictionary(), 4)
            elif clientInput == "stop":
                return user
        else:
            getter = "\nThat did not make sense my friend, pardon me, but I would like you to repeat that."
            getoncemore(rule.get_query(), getter, conn)
    elif input_index == 2:
        if int(clientInput) not in range(1, 5) and clientInput != "stop":
            getter = "\nThat did not make sense my friend, pardon me, but I would like you to repeat that."
            getoncemore(rule.get_query(), getter, conn)
        elif int(clientInput) in range(1, 5):
            print("\n Valid Input")
            user.setcategoryvals(rule.get_category_dictionary(), int(clientInput))
        elif clientInput == "stop":
            return user
    return user


def checkbase(rule, clientInput, conn, user):
    if clientInput == "no":
        DisorderCategories.purge(3, DisorderCategories.RuleDict)
        print("Valid input")
        return True
    elif clientInput == "yes":
        return True
    elif clientInput == "stop":
        path = "Data/" + user.name + ".p"
        RulesDefiner.save_object(user, path)
        return user
    else:
        getoncemore(rule.get_query(), rule.get_query(), conn)


def resetAll():
    RulesDefiner.resetglobals()


if __name__ == '__main__':
    server_program()

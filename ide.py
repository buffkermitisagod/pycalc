def main():
    import sys

    # will remake in c++ as it is faster
    # compiler

    vdr = ["[START_vdr]"]

        
    def ter(var, i): # get rid of stored veriable made easy
        i = i.replace("ter","")
        i = i.replace(" ","")
        i = i.replace("\n","")
        r = str(i)
        x = var.index(r)
        o = var[x+1]
        var.remove(r)
        var.remove(o)
        return var # return edited list

    def ver(var, i):
        if "int" in i:
            # calculate
            xx = i.split("=")
            chk = xx[0]
            chk = chk.replace("int","")
            f = chk.replace(" ","")
            if f in var:
                print("[!] ERROR ("+f+") already defined is term "+f+" to termnate it")
                input("")
            else:
                calc = xx[1]
                calc = calc.replace("'","")
                calc = calc.replace("\n","")
                calc = calc.replace(" ","")
                x = calc
                #all calculations
                ##############################
                if "+" in x: 
                    x = x.split("+") # split at x where x is the calculation
                    try:
                        num1 = int(x[0]) # try get num 2 as intger if not then must be verable already stored eg c
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num1 = int(var[num+1]) # get value of x where x is verable eg c
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    try:
                        num2 = int(x[1]) # same as for num1
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num2 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    c = num1 + num2 # do calculation
                ##########################
                # this wll explain for the
                # entire calculations bit
                #########################
                elif "/" in x:
                    x = x.split("/")
                    try:
                        num1 = int(x[0])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num1 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    try:
                        num2 = int(x[1])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num2 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    c = num1 / num2
                elif "*" in x:
                    x = x.split("*")
                    try:
                        num1 = int(x[0])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num1 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    try:
                        num2 = int(x[1])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num2 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    c = num1 * num2
                elif "-" in x:
                    x = x.split("-")
                    try:
                        num1 = int(x[0])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num1 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    try:
                        num2 = int(x[1])
                    except ValueError:
                        try:
                            n = x[0]
                            num = var.index(n)
                            num2 = int(var[num+1])
                        except ValueError: # check if veriable exits
                            print("[!] ERROR ("+n+") dosen't exist")
                            input("")
                    c = num1 - num2
                else:
                    pass
                v = xx[0]
                v = v.replace("int","")
                v = v.replace(" ","")
                x = v
                var.append(x)
                b = str(c)
                var.append(b)
            return var

    def pri(var, i):
        x = i.split("PRINT: ") 
        x = x[1]
        x.replace(" ","")
        x.replace("\n","")
        if '"' not in i: # if veriable
            xx = 0
            for f in var: #will change but keep for now
                if f in x:
                    print(var[xx+1]) # find it
                    #
                else:
                    xx = xx + 1
                        
        else:
            x = x.replace('"','')
            print(x)
            
####################################
#         if statemnts             #
####################################

    def __if_(var, i, num):
        br = i.split("{")
        i = br[0]
        br = br[1]
        br = br.replace("}","")
        br = br.replace("\n","")
        br = br.rsplit(";")
        
        i = i.replace("if","")
        i = i.replace(" ","")
        i = i.replace("\n","")    
        i = i.split("<")
        
        chk = i[1]
        i = i[0]
        try:
            chk = int(chk)
        except ValueError:
            try:
                n = chk
                num = var.index(n)
                chk = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
        try:
            i = int(i)
        except ValueError:
            try:
                n = i
                num = var.index(n)
                i = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
                
        #############################################
        # run if statements
        
        if i < chk:
            for v in br:
                if "PRINT:" in v:
                    pri(var, v)
                if "=" in v:
                    r = ver(var, v)
                    var = r
                if "ter" in v:
                    r = ter(var, v)
                    var = r
                    
        ########################################
        return var
    
    def _if__(var, i, num):
        br = i.split("{")
        i = br[0]
        br = br[1]
        br = br.replace("}","")
        br = br.replace("\n","")
        br = br.rsplit(";")
        
        i = i.replace("if","")
        i = i.replace(" ","")
        i = i.replace("\n","")    
        i = i.split(">")
        
        chk = i[1]
        i = i[0]
        try:
            chk = int(chk)
        except ValueError:
            try:
                n = chk
                num = var.index(n)
                chk = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
        try:
            i = int(i)
        except ValueError:
            try:
                n = i
                num = var.index(n)
                i = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
                
        #############################################
        # run if statements
        
        if i > chk:
            for v in br:
                if "PRINT:" in v:
                    pri(var, v)
                if "=" in v:
                    r = ver(var, v)
                    var = r
                if "ter" in v:
                    r = ter(var, v)
                    var = r
                    
        ########################################
        return var
    
    def _if_(var, i, num):
        br = i.split("{")
        i = br[0]
        br = br[1]
        br = br.replace("}","")
        br = br.replace("\n","")
        br = br.rsplit(";")
        
        i = i.replace("if","")
        i = i.replace(" ","")
        i = i.replace("\n","")    
        i = i.split("=")
        
        chk = i[1]
        i = i[0]
        try:
            chk = int(chk)
        except ValueError:
            try:
                n = chk
                num = var.index(n)
                chk = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
        try:
            i = int(i)
        except ValueError:
            try:
                n = i
                num = var.index(n)
                i = int(var[num+1])
            except ValueError: # check if veriable exits
                print("[!] ERROR ("+n+") dosen't exist")
                input("")
                
        #############################################
        # run if statements
        
        if i == chk:
            for v in br:
                if "PRINT:" in v:
                    pri(var, v)
                if "=" in v:
                    r = ver(var, v)
                    var = r
                if "ter" in v:
                    r = ter(var, v)
                    var = r
                    
        ########################################
        return var
    
###########################################################

    print("[START]") #c = 1 + 1
    while True:
        v = input("PYCALC > ")
        # print
        if "PRINT:" in v:
            pri(vdr, v)
                
        if "=" in v:
            r = ver(vdr, v)
            vdr = r
        if "ter" in v:
            r = ter(vdr, v)
            vdr = r
        else:
            pass
        #print("[VARS] ", var)
    print("\n\n[DONE]")


import os

def infoga(input:str):


    for count,info in enumerate(input) :
        s = info['data']
        curPath = os.getcwd()
        os.system(f' {curPath}\Infoga\infoga.py" --info {s} --breach -v 3 --report reports/infogaOutput.txt')
        try : 
            file = open('reports/infogaOutput.txt')
            data = file.read()
            file.close()
            if "This email wasn't leaked" in data:
                info['data'] = s+' (not breach)'
            else:
                info['data'] = s+' (breach)'
            input[count]= info     
        except:
            continue
    return input




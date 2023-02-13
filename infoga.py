
import os

def infoga(input:str):


    for count,info in enumerate(input) :
        s = info['data']
        curPath = os.getcwd()
        try : 
            os.system(f'python "{curPath}\infoga\infoga.py" --info {s} --breach -v 3 --report reports/infogaOutput.txt')
            file = open('reports/infogaOutput.txt')
            data = file.read()
            file.close()
            if "This email wasn't leaked" in data:
                info['data'] = s+' (not breach)'
            else:
                info['data'] = s+' (breach)'
            input[count]= info     
        except:
            print('invalid email')
    return input


# infoga([{'data' :'สอบถามข้อมูลเพิ่มเติมติดต่อคุณเด่น095-437-7275Email:den.tup@mahidol.ac.thหรือคุณสารัชย์092-256-1570Email:sarachaya.chi@mahidol.ac.th'}])

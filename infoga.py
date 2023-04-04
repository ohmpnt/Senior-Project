
import os

def infoga(input:list):

    # loop though each email
    for count,info in enumerate(input) :
        s = info['data']
        curPath = os.getcwd()
        try : 
            os.system(f'python "{curPath}\infoga\infoga.py" --info {s} --breach -v 3 --report reports/infogaOutput.txt') # call infoga
            file = open('reports/infogaOutput.txt') # open the report file
            data = file.read() #read the report
            file.close()
            # check weather the email is breach or not
            if "This email wasn't leaked" in data:
                info['data'] = s+' (not breach)'
            else:
                info['data'] = s+' (breach)'
            input[count]= info     
        except:
            print('invalid email')
    return input




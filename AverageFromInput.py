#Michael Sherrer
#CS 175L
#AverageFromInput Assignment with Exception

def values():
    numbers_file=open('numbers.txt','r')
    line=numbers_file.readline()
    while line!='':
        current_number=float(line)
        line=numbers_file.readline()
        return current_number
    numbers_file.close()

def average():
    num_lines=0
    total=0.0
    numbers_file=open('numbers.txt','r')
    line=numbers_file.readline()
    for line in numbers_file:
        current_number=float(line)
        total+=current_number
        num_lines+=1
    average=total/num_lines
    return average

def error_check(average):
    print('Average of the numbers:',average)
    try:
        numbers_file=open('numbers.txt','r')
    except IOError:
        print('An error occured trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    

def main():
    values()
    average()
    error_check()
    
if __name__=='__main__':
    main()

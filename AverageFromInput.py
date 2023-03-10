#Michael Sherrer
#CS 175L
#AverageFromInput Assignment

def main():
    total=0
    read_in=0
    numbers_file=open('numbers.txt','r')
    for line in numbers_file:
        current_number=float(line)
        read_in+=1
        total+=current_number
        print('I read in',read_in,'numbers(s), Current number is:',
              current_number,'Total is:',total)
    numbers_file.close()

if __name__=='__main__':
    main()

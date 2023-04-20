#Michael Sherrer
#expensePieChart
#CS175-L

import matplotlib.pyplot as plt

def read_expenses(filename):
    expenses={}
    with open(filename) as f:
        for line in f:
            try:
                label,value=line.strip().split('\t')
                expenses[label]=int(value)
            except ValueError:
                print(f'Invalid value on line: {line.strip()}')
    return expenses

def expense_pie_chart(expenses):
    labels=expenses.keys()
    values=expenses.values()
    plt.pie(values,labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def main():
    filename='expenses.txt'
    try:
        expenses=read_expenses(filename)
        expense_pie_chart(expenses)
    except IOError:
        print(f'File cannot be opened: {filename}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()


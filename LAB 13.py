def userGreeting():
    
    # User greetings
    print('Welcome to the conversion program')
    print()
    
    # Displays all conversion choices user can do
    print('Enter I to convert from Inches to Centimeters')
    print('Enter C to convert from Centimeters to Inches')
    print('Enter O to convert from Ounces to Grams')
    print('Enter G to convert from Grams to Ounces')
    print('Enter M to convert from Miles to kilometers')
    print('Enter K to convert from kilometers to Miles')
    print()
    
def userChoice():
    
    # Get user input conversion
    conversionUnit = input('Enter the type of conversion you would like to do: ').upper()
    print()
    
          
    # Error check program
    while conversionUnit not in ['I', 'C', 'O', 'G', 'M', 'K']:
        conversionUnit = input('INPUT ERROR: Please enter a I or C or O or G or M or K: ').upper()

    # Get user input measure/weight
    measure = float(input('Enter a measure/weight you want to convert: '))
    print()
    return conversionUnit, measure
 
def doCalculations(conversionUnit, measure):
    
    # Do conversions, calculations and display results
    if conversionUnit == 'I':
        measureConvert = measure * 2.54
        print(measure,'inches equals', format(measureConvert, ',.2f'), 'centimeters')
    elif conversionUnit == 'C':
        measureConvert = measure / 2.54
        print(measure, 'centimeters equals', format(measureConvert, ',.2f'), 'inches')
    elif conversionUnit == 'O':
        measureConvert = measure * 28.3495231
        print(measure, 'ounces equals', format(measureConvert, ',.2f'), 'grams')
    elif conversionUnit == 'G':
        measureConvert = measure / 28.3495231
        print(measure, 'grams equals', format(measureConvert, ',.2f'), 'ounces')
    elif conversionUnit == 'M':
        measureConvert = measure * 1.609344
        print(measure, 'miles equals', format(measureConvert, ',.2f'), 'kilometers')
    else:
        measureConvert = measure / 1.609344
        print(measure, 'kilometers equals', format(measureConvert, ',.2f'), 'miles')
        print()
        
def programLoop():
    
    # Program loop
    run = input('Would you like to make another conversion?(yes/no) ').lower()
    print()
        
    # Error check loop
    while run != 'yes' and run != 'no':
        run = input('INPUT ERROR: Please type a yes or no: ').lower()
        print()
        
    return run
            
def exitMessage():
    
    # Exit message
    print ('Have a nice day!!!!')

    
# -------------------------------------------------MAIN-------------------------------------------
userGreeting()

# Start of a while loop
run = 'yes'
while run == 'yes':
    
    # user inputs
    conversionUnitMain, measureMain = userChoice()
    
    # calculates conversion
    doCalculations(conversionUnitMain, measureMain)

    # asks user if they would like to re-run the code
    run = programLoop()
        
# exits message
exitMessage()
    







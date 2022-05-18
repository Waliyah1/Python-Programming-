#Exercise 3
#Grade = int(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
Score = float(input('Enter score:'))
if Score >= 0.9:
    print ('A')
elif Score >= 0.8:
    print ('B') 
elif Score >= 0.7:
    print ('C')
elif Score >= 0.6:
    print ('D')
elif Score < 0.6:
    print ('F')
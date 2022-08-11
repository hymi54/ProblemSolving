month, day = map(int, input().split())

cal = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}

match (cal[month]+day) % 7:
    case 1:
        print('MON')
    case 2:
        print('TUE')
    case 3:
        print('WED')
    case 4:
        print('THU')
    case 5:
        print('FRI')
    case 6:
        print('SAT')
    case 0:
        print('SUN')

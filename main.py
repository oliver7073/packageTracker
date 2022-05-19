from packageStatus import packageStatus
from findCarriers import findCarriers
from createTracking import createTracking

while True:
    try:
        feature = int(input("Please choose a feature:\n" + "1: Get package status\n" + "2: Get couriers\n" + "3: Input package into system\n"))
    except ValueError:
        print("Error, please try again\n")
        continue

    if (feature < 0) or (feature > 3):
        print("Error, please try again\n")
    else:
        break
        
if int(feature) == 1:
    courier = input("Input the courier: ")
    trackingNumber = input("Input the tracking number: ")
    packageStatus(courier, trackingNumber)

elif int(feature) == 2:
    tracking = input("Input your tracking number: ")
    findCarriers(tracking)

elif int(feature) == 3:
    title = input("Input the name of the package: ")
    courier = input("Input the courier of the package: ")
    trackingNumber = input("Input your tracking number: ")
    createTracking(title, courier, trackingNumber)


















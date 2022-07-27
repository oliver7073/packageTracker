# Package Tracker

A package tracker that allows the user to input and store their packages to a AfterShip me account and is able to retrieve the status of it using the AfterShip API.
There is a feature that gets all of the possible couriers of a tracking number.

# Setting up
To get started, first  clone the repo and open the files in your prefered IDE. Then sign up for an [Aftership](https://www.aftership.com/) account and obtain the API key. Edit the ``findCarriers.py``,``packageStatus.py``, and ``createTracking.py`` files and replace the text "INPUT API KEY" with your API key. After that, you are able to run the ``main.py`` file and the three choices appear.

![main](https://user-images.githubusercontent.com/43973602/181116383-3876bd9c-3dda-48de-816f-d6cb29406b91.png)


# 1. Inputting packages into system
This feature adds and stores a package to the user's AfterShip account. When choosing this feature, it would prompt the user to input the name of the package, courier, and the tracking number.

![adding package](https://user-images.githubusercontent.com/43973602/181126321-0abd749c-bd06-456d-b9cc-27cdd7ba2fe3.png)


# 2. Get couriers
This feature returns a list of all the possible couriers of an inputted tracking number. When selecting this option, input the tracking number when prompted.

![get couriers](https://user-images.githubusercontent.com/43973602/181125509-b27a0566-eaa0-4295-9efe-9199b8bdb8b9.png)


# 3. Get package status
To get the status of your package, you would first have to input the packages into the system, which is the first option. Once it is in the system, you can then input the courier and the tracking number. There is additional information that can be returned in the ``packageStatus.py``  by uncommenting the lines of code.

![status](https://user-images.githubusercontent.com/43973602/181124635-1da249a7-c865-43e9-9345-a83d35bcf01e.png)







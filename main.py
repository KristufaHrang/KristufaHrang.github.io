# Importing needed libraries
from http import server
from typing import final
from unicodedata import name
from urllib import response
import requests
import json
import time
import os
from termcolor import colored
from win10toast import ToastNotifier
import urllib3

# Disables the warning for Verify=False as this will make the program break from the API
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Creates the notifications and sets their variables
toast = ToastNotifier()
errortoast = ToastNotifier()
toast429 = ToastNotifier()
toast403 = ToastNotifier()
toast404 = ToastNotifier()
toast408=ToastNotifier()

# Creates the welcome function
def welcome():
    # Globals the variables listed below so other functions can use them outside of this function
    global accountanswer
    global accountname
    global accounttag
    global accountregion

    # Greets the user and asks for their account name and tag, which the API will check for this account
    print("Welcome to StatTracker, one of the best ways to understand you as a player and to improve.")
    accountname = input("To begin, enter your VALORANT name below. \n\n")
    accounttag = input("\nNearly there.. now enter your VALORANT tag below.\n\n")
    print("Please what while we check for your account...")
    accounturl = "https://api.henrikdev.xyz/valorant/v1/account/"+ accountname + "/" + accounttag + "?force=true/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    accountresult = requests.get(accounturl, headers=headers, verify=False)
    accountanswer = accountresult.text

    # If the status responds with a success code, tell the user then head to the mainmenu function
    if json.loads(accountanswer)["status"] == 200:
        accountregion = json.loads(accountanswer)["data"]["region"]
        print("Account found!")
        time.sleep(3)
        os.system('cls')
        print("Welcome, " + accountname + " #" + accounttag)
        print("You are now being put in the main menu of StatTracker for VALORANT.")
        time.sleep(2)
        print("Your stats, recent games and more will show up there.")
        time.sleep(5)
        os.system('cls')
        print("Please wait.. gettting account information and stats.")
        print("Hold tight!")
        mainmenu()

        # If the status responds with an 404 code, tell the user they maybe made a typo as the account was not found
    elif json.loads(accountanswer)["status"] == 404:

        toast404.show_toast(
            "Error!",
            "Error code: 404. \nAccount not found, did you make a typo?",
            duration = 5,
            threaded = True,
    )
        os.system('cls')
        print("Your account was not found, please try again.")
        print("Have you made a typo?")
        time.sleep(1)
        print("Going back in 3...")
        time.sleep(1)
        print("Going back in 2...")
        time.sleep(1)
        print("Going back in 1...")
        time.sleep(1)
        os.system('cls')
        welcome()

        # If the status is 403 or 503, tell the user that an error occured and  the user can troubleshoot, quit or go back.
    elif json.loads(accountanswer)["status"] == 403 or 503:

        toast403.show_toast(
        "Error!",
        "Error code 403 or 503 \nThe API request made to Riot was forbidden to connect.\nTry again later.",
        duration = 5,
        threaded = True,
    )

        os.system('cls')
        print("ERROR: A request was made to the Riot API, but it was forbidden to connect.")
        print("Status code: 403 or 503")
        print("This probably occured because the Riot API is currently under maintanence for patches and updates or the internet you are using has forbidden this URL.")
        print("Hint: If you are at school running this and seeing this error, go into the file and change line 24 and add , verify=False at the end.")
        print("This error will usually resolve itself within 30 minutes.")

        def gobackorexit():
                yesorno = input("Do you want to exit program, go back or troubleshoot? \n Acceptable answers: exit, go back, troubleshoot.\n")
                if yesorno == "exit":
                    exit()

                elif yesorno == "go back":
                    welcome()
                
                elif yesorno == "troubleshoot":
                    print("WARNING THIS MODE IS FOR DEVELOPERS ONLY.")
                    print("TO EXIT THIS MODE SIMPLY CLOSE THE PROGRAM.")
                    print("Continuing in 10 seconds...")
                    time.sleep(10)
                    print("Currently running pre-alpha V.0.0.1")
                    time.sleep(2)
                    print(accountanswer)
                    print("\nThis is what the API returned with. This is all the data it responded with.")
                    time.sleep(3)
                    
                    print("\nThis is the only data given.")

                else:
                    print("Sorry, that is not an acceptable answer. \n")
                    time.sleep(2)
                    os.system('cls')
                    gobackorexit()

        gobackorexit()

        # If the status responds with code 408, tell the user that the request timed out and the user can then go back, exit or troubleshoot
    elif json.loads(accountanswer)["status"] == 408:

        toast408.show_toast(
        "Error!",
        "Error code 408 \nThe API request made to Riot timed out.\nTry again later.",
        duration = 5,
        threaded = True,
    )

        os.system('cls')
        print("ERROR: A request was made to the Riot API, but the request timed out.")
        print("Status code: 408")
        print("This is probbaly due to your network being really slow or an error occured.")
        print("Hint: Try to restart your router or check your internet connection.")

        def gobackorno():
                yesorno = input("Do you want to exit program, go back or troubleshoot? \n Acceptable answers: exit, go back, troubleshoot.\n")
                if yesorno == "exit":
                    exit()

                elif yesorno == "go back":
                    welcome()
                
                elif yesorno == "troubleshoot":
                    print("WARNING THIS MODE IS FOR DEVELOPERS ONLY.")
                    print("TO EXIT THIS MODE SIMPLY CLOSE THE PROGRAM.")
                    print("Currently running pre-alpha V.0.0.1")
                    print("Continuing in 10 seconds...")
                    time.sleep(10)
                    print(accountanswer)
                    print("\nThis is what the API returned with. This is all the data it responded with.")
                    time.sleep(3)
                    print("\nThis is the only data given.")

                else:
                    print("Sorry, that is not an acceptable answer. \n")
                    time.sleep(2)
                    os.system('cls')
                    gobackorno()

        gobackorno()
        
        # If the status responds with status 429, tell the user the rate limit was reached and then they can go back, exit or troubleshoot
    elif json.loads(accountanswer)["status"] == 429:

        toast429.show_toast(
        "Error!",
        "Error code 429\nThe rate limit for this API has been reached.\nTry again later.",
        duration = 5,
        threaded = True,
    )

        os.system('cls')
        print("ERROR: A request was made to the Riot API, but the rate limit for requests has been reached.")
        print("This means that the amount of information this program is able to request has been reached.")
        print("This error resolves itself by time, so check back in 2 1/2 minutes time")

        def wannagoback():
                yesorno = input("Do you want to exit program, go back or troubleshoot? \n Acceptable answers: exit, go back, troubleshoot.\n")
                if yesorno == "exit":
                    exit()

                elif yesorno == "go back":
                    welcome()
                
                elif yesorno == "troubleshoot":
                    print("WARNING THIS MODE IS FOR DEVELOPERS ONLY.")
                    print("TO EXIT THIS MODE SIMPLY CLOSE THE PROGRAM.")
                    print("Currently running pre-alpha V.0.0.1")
                    print("Continuing in 10 seconds...")
                    time.sleep(10)
                    print(accountanswer)
                    print("\nThis is what the API returned with. This is all the data it responded with.")
                    print("\nRate limits using this API is limited to 250 requests every 2.5 minutes.")
                    time.sleep(3)
                    print("\nThis is the only data given.")

                else:
                    print("Sorry, that is not an acceptable answer. \n")
                    time.sleep(2)
                    os.system('cls')
                    wannagoback()

        wannagoback()

# The main menu function
def mainmenu():

    # Asks the API for information about the users MMR.
    accountelo = "https://api.henrikdev.xyz/valorant/v1/mmr-history/" + accountregion + "/"  + accountname + "/" + accounttag
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    accounteloresult = requests.get(accountelo, headers=headers, verify=False)
    accounteloanswer = accounteloresult.text
    currentelo = json.loads(accounteloanswer)["data"][0]["currenttierpatched"]
    rankingincurrentelo = json.loads(accounteloanswer)["data"][0]["ranking_in_tier"]

    # States what account the user has logged in as
    os.system('cls')
    print("Now logged in as: " + accountname + " #" + accounttag)

    # States the user's current rank
    print("Your current rank")
    print(str(currentelo) + " " + str(rankingincurrentelo) + "/100")

    # Asks the API for information about the users match history and performance
    matchhistory = "https://api.henrikdev.xyz/valorant/v3/matches/" + accountregion + "/" + accountname + "/" +accounttag +"?filter=competitive"
    matchhistoryresult = requests.get(matchhistory, headers=headers, verify=False)
    matchhistoryanswer = matchhistoryresult.text

    # Gets the player's death and kills and what map they played on
    averagek1 = json.loads(matchhistoryanswer)["data"][0]["players"]["all_players"][0]["stats"]["kills"]
    averaged1 = json.loads(matchhistoryanswer)["data"][0]["players"]["all_players"][0]["stats"]["deaths"]
    match1 = json.loads(matchhistoryanswer)["data"][0]["metadata"]["map"]

    # Same as above, except for the second map they played
    averagek2 = json.loads(matchhistoryanswer)["data"][1]["players"]["all_players"][0]["stats"]["kills"]
    averaged2 = json.loads(matchhistoryanswer)["data"][1]["players"]["all_players"][0]["stats"]["deaths"]
    match2 = json.loads(matchhistoryanswer)["data"][1]["metadata"]["map"]

    # Same as above, except for the third map they played
    averagek3 = json.loads(matchhistoryanswer)["data"][2]["players"]["all_players"][0]["stats"]["kills"]
    averaged3 = json.loads(matchhistoryanswer)["data"][2]["players"]["all_players"][0]["stats"]["deaths"]
    match3 = json.loads(matchhistoryanswer)["data"][2]["metadata"]["map"]

    # Averages the Kills from the three maps
    averagekpart1 = int(averagek1)+int(averagek2)+int(averagek3)
    averagekpart2 = int(averagekpart1)/3

    # Averages the Deaths from the three maps
    averagedpart1 = int(averaged1)+int(averaged2)+int(averaged3)
    averagedpart2 = int(averagedpart1)/3

    # Adds the KD then divides to find the average
    finalkd1 = int(averagekpart2) + int(averagedpart2)
    finalkd = int(averagekpart2)/int(averagedpart2)

    # If the data couldnt be retrieved from the API (Status other than 200 which is the success status) then tell the user an error occured and show a notification
    if json.loads(matchhistoryanswer)["status"] != 200:

        errortoast.show_toast(
            "Error!",
            "An error occured and the data couldn't be pulled from the API.",
            duration = 5,
            threaded = True,
    )
        print("Error: An error occured and the data couldn't be pulled from the API.")
        print("This may be because the connection refused to connect, timed out or the rate limit for this API has been reached")

        # Asks the user whether they want to leave, go back or troubleshoot the issue
        # If user says exit then close the program
        # If user says go back, go back to mainmenu()
        # If user says troubleshoot then warn them about entering developer mode then tell the user about the API response and what version they're running
        # If the user has an invalid input, warn them and go back to start of this function()
        def troublegobackexit():
            global gobackornot
            gobackornot = input("Do you want to exit program, go back or troubleshoot? \n Acceptable answers: exit, go back, troubleshoot.\n")

            if gobackornot == "exit":
                exit()

            elif gobackornot == "go back":
                mainmenu()
                
            elif gobackornot == "troubleshoot":
                print("WARNING THIS MODE IS FOR DEVELOPERS ONLY.")
                print("TO EXIT THIS MODE SIMPLY CLOSE THE PROGRAM.")
                print("Continuing in 10 seconds...")
                time.sleep(10)
                print("Currently running pre-alpha V.0.0.1")
                time.sleep(2)
                print(matchhistoryanswer)
                print("\nThis is what the API returned with. This is all the data it responded with.")
                time.sleep(3)
                    
                print("\nThis is the only data given.")

            else:
                print("Sorry, that is not an acceptable answer. \n")
                time.sleep(2)
                os.system('cls')
                gobackornot()

        gobackornot()

    # Prints the users average KD from the past 3 games in Competitive
    print("\nYour average KD from the past 3 games in Competitive")
    print("(" + match1 + ", " + match2 + " and " + match3+")")
    finalkdbutrounded = (round(finalkd, 2))
    print(finalkdbutrounded)

    if finalkdbutrounded < 1:
        positivekd = False
    elif finalkdbutrounded >= 1:
        positivekd = True

    # Asks the API for the player's headshots from the last three games
    headshot1 = json.loads(matchhistoryanswer)["data"][0]["players"]["all_players"][0]["stats"]["headshots"]
    headshot2 = json.loads(matchhistoryanswer)["data"][1]["players"]["all_players"][0]["stats"]["headshots"]
    headshot3 = json.loads(matchhistoryanswer)["data"][2]["players"]["all_players"][0]["stats"]["headshots"]

    # Asks the API for the player's letgshots from the last three games
    legshot1 = json.loads(matchhistoryanswer)["data"][0]["players"]["all_players"][0]["stats"]["legshots"]
    legshot2 = json.loads(matchhistoryanswer)["data"][1]["players"]["all_players"][0]["stats"]["legshots"]
    legshot3 = json.loads(matchhistoryanswer)["data"][2]["players"]["all_players"][0]["stats"]["legshots"]

    # Asks the API for the player's bodyshots from the last three games
    bodyshot1 =  json.loads(matchhistoryanswer)["data"][0]["players"]["all_players"][0]["stats"]["bodyshots"]
    bodyshot2 =  json.loads(matchhistoryanswer)["data"][1]["players"]["all_players"][0]["stats"]["bodyshots"]
    bodyshot3 =  json.loads(matchhistoryanswer)["data"][2]["players"]["all_players"][0]["stats"]["bodyshots"]

    # Averages the headshot, legshot and bodyshots from the last three games and rounds them to the nearest unit
    headshotaverage1 = int(headshot1) + int(headshot2) + int(headshot3)
    headshotaverage2 = int(headshotaverage1)/3
    roundedheadshot = round(headshotaverage2)

    legshotaverage1 = int(legshot1) + int(legshot2) + int(legshot3)
    legshotaverage2 = int(legshotaverage1)/3
    roundedlegshot = round(legshotaverage2)

    bodyshotaverage1 = int(bodyshot1) + int(bodyshot2) + int(bodyshot3)
    bodyshotaverage2 = int(bodyshotaverage1)/3
    roundedbody = round(bodyshotaverage2)

    # Prints out the user's average headshot, legshots and bodyshots
    print("\nYour average hits from the past 3 games in Competitive")
    
    print("Headshots: " + str(roundedheadshot) +" hits")
    print("Bodyshots: " + str(roundedbody) + " hits")
    print("Legshots: " + str(roundedlegshot) + " hits")

    # Asks the user what they want to do
    print("\nYou are now able to analyse your stats.")
    print("(1) Analyse your rank")
    print("(2) Analyse your KD")
    print("(3) Analyse your hit distribution")
    print("(4) Logout")
    print("Quit to quit the program")
    time.sleep(1)
    analyse = input("What would you like to do?\n")

    # Asks the user whether they want to leave, or go back. If the user enters an invalid option, warn them then repeat.
    def wannaleave():
        print("What would you like to do?")
        gobacktomainmenu1 = input("Acceptable answers: go back or quit.\n")

        if gobacktomainmenu1 == "go back":
            mainmenu()
        elif gobacktomainmenu1 == "quit":
             exit()
        else:
            print("Sorry, that is not an acceptable answer. \n")
            time.sleep(2)
            os.system('cls')
            wannaleave()

    # If 1 is entered, print the user's rank and tell the user about the ranks and what to do and calls to the wannaleave function
    if analyse == "1":
        os.system('cls')
        print("Your current rank is " + str(currentelo) + " " + str(rankingincurrentelo) + "/100")
        print("If your rank is lower than platinum, you are in low elo. If higher than platinum, then you are in high elo.")
        print("If you are in one of the lower elos, try to communicate with your teammates more through team chat.")
        print("This can help coordinate as a team and easily win rounds, and in-turn, your rank will increase.")
        time.sleep(5)
        print("\n")
        wannaleave()

        # If 2 is entered, print the user's KD and tell the user about what it is, and what to do. Then calls to the wannaleave function
    elif analyse == "2":
        os.system('cls')
        print("Your current KD from the past three games is "+ str(finalkdbutrounded))

        if positivekd == True:
                print("Your KD is positive! Keep it up!")
        elif positivekd == False:
            print("Your KD is negative, which isn't that good.")

        print("\nIf your KD is negative, then try to take more safe duels instead of rushing on site and quickly getting mowed down by the enemy team.")
        print("Also try to play as a team, 5 people compared to 2 or so on site will be a clean sweep.")
        print("All of these strats should improve your KD!")
        time.sleep(5)
        print("\n")
        wannaleave()
        
        # If 3 is entered, print the user's average hits on the enemy's body, what it is, and what to do. Then calls to the wannaleave function
    elif analyse == "3":
        os.system('cls')
        print("Your current hit distubition is as follows:")
        print("Headshots: " + str(roundedheadshot) +" hits")
        print("Bodyshots: " + str(roundedbody) + " hits")
        print("Legshots: " + str(roundedlegshot) + " hits\n")
        print("If your headshots seem incomparable to your bodyshots or headshots, try lifting your cursor up.")
        print("Not only will you get a better crosshair placement, but more kills.")
        print("Try heading over to a custom game, then try clearing corners with good crosshair placement.")
        print("Alternatively, install Aim Labs from the steam store for free and go through some of their training tools.")
        time.sleep(5)
        print("\n")
        wannaleave()

        # If 4 is entered, log the user out and go back to welcome.
    elif analyse == "4":
        os.system('cls')
        print("You are now about to log out, thank you for using StatTracker!")
        print("Good luck in your games!")
        time.sleep(2)
        print("Continuing in 3...")
        time.sleep(1)
        print("Continuing in 2...")
        time.sleep(1)
        print("Continuing in 1...")
        time.sleep(1)
        os.system('cls')
        welcome()

        # If quit is entered, thank the user for using this software then exit
    elif analyse == "quit" or "Quit":
        os.system('cls')
        print("Thank you for using StatTracker!")
        print("Good luck in your games!")
        print("GLHF!")
        time.sleep(5)
        quit()

        # If the user enters an unacceptable answer, tell them then loop back to main menu function
    else:
        print("\nSorry, that is not an acceptable answer. \n")
        time.sleep(2)
        os.system('cls')
        mainmenu()

# Clears the screen
os.system('cls')

# Welcomes the user through a notification
toast.show_toast(
        "Welcome!",
        "Welcome to StatTracker.",
         duration = 5,
        threaded = True,
    )

# Calls to the welcome function
welcome()
from queueADT import *
from random import randint

class passenger:
    def __init__(self, pID, ArrivalTime):
        self._pID =pID
        self._arraivalTime = ArrivalTime

    # Return id Number
    def getPID(self):
        return self._pID

    # Return Arrival Time
    def timeArrived(self):
        return self._arraivalTime

class TicketAgent:
    def __init__(self, aID):
        self._aID = aID
        self._passenger = None
        self._stopTime = -1
    # Return Id Number
    def getAID(self):
        return self._aID

    # Determine if Agent is Free
    def isFree(self):
        return self._passenger is None

    # Determine if Agent has finished a Service
    def isFinished(self, curTime):
        return self._passenger is not None and curTime == self._stopTime


    # Start Attending to a Passenger
    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    # Stop Service to a Passenger
    def stopService(self):
        thepassenger =self._passenger
        self._passenger = None
        return thepassenger


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        #Parameters supplied by the user
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0

        # Simulation components.
        self._passengers = CircularQueue()
        self._Agents = [None] * numAgents
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival ( curTime)
            self._handleBeginService( curTime )
            self._handleEndService( curTime )
        self.printResult()


    def printResult(self):
        numServed = self._numPassengers - len(self._passengers)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print(f"Number or passengers served = {numServed}")
        print(f"Number of passengers remaining in line = {len(self._passengers)}")
        print(f"The average wait time was {avgwait :.2f} minutes.")


    # Handle Customer Arrival
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if 0.0 <= prob <= self._arriveprob:
            person = passenger(self._numPassengers + 1, curTime)
            self._passengers.enqueue( person )
            self._numPassengers += 1
            print( f"Time {curTime} : Passenger {person.getPID()} arrived.")



    # Begin Customer Service
    def _handleBeginService(self, curTime):

        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passengers.isEmpty() and curTime != self._numMinutes:
                passenger = self._passengers.dequeue()
                self.served += 1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger, stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrived())
                print(f"Time {curTime} : Agent {self._Agents[i].getAID()} started serving passenger {passenger.getPID()}")
            i += 1



    # Stop Customer Service
    def _handleEndService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print(f"Time {curTime} : Agent {self._Agents[i].getAID()} stopped serving passenger {passenger.getPID()} ")
            i += 1


"""My Life cycle"""

from random import random

def prime(func):
    """Prime method function"""
    def wrapper(*args, **kwargs):
        var = func(*args, **kwargs)
        var.send(None)
        return var
    return wrapper


class FSM:
    """FSM class for my life cycle"""
    def __init__(self):
        # initializing states
        self.start = self._create_start()
        self.sleep = self._sleep()
        self.eat = self._eat()
        self.work = self._work()
        self.play = self._play()
        self.chat = self._chat()
        self.holidays = self._holidays()
        # setting current state of the system
        self.current_state = self.start

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

    def send(self, char):
        """The function sends the curretn input to the current state
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        """The function at any point in time returns if till the current input
        the string matches the given regular expression.

        It does so by comparing the current state with the end state 'holidays'.
        It also checks for `stopped` flag which sees that due to bad input
        the iteration of FSM had to be stopped.
        """
        if self.stopped:
            return False
        return self.current_state == self.holidays

    def _holidays(self):
        while True:
            _ = yield
            break

    def _create_start(self):
        while True:
            hour = yield
            if hour >= 0 and hour <=7:
                self.current_state = self.sleep
            elif hour > 7 and hour <=8:
                self.current_state = self.eat
            elif hour >=9 and hour <=18:
                self.current_state = self.eat
            break
    @prime
    def _sleep(self):
        while True:
            hour = yield
            if random() == 1:
                print("FINALLY, work is done, holidays are on")
                self.current_state = self.holidays
                break
            elif random() >= 0.5 and hour > 7 and hour <=8 :
                print("I'm in mood for a breakfast today")
                self.current_state = self.eat
            elif hour == 9:
                print("Who cares about nutrition? I'll eat later")
                self.current_state = self.work
            else:
                print("zzz...")
    @prime
    def _eat(self):
        while True:
            hour = yield
            if random() == 1:
                print("FINALLY, work is done, holidays are on")
                self.current_state = self.holidays
                break
            elif hour == 18:
                print("Yep, I love dnd")
                self.current_state = self.play
            elif hour == 11:
                print("I ate, now work, but maybe I should grab some coffee first...")
                self.current_state = self.work
            else:
                print("Still eating...")
    @prime
    def _play(self):
        while True:

            hour = yield
            if random() == 1:
                print("FINALLY, work is done, holidays are on")
                self.current_state = self.holidays
                break
            elif hour >= 0 and hour <=7:
                print("That was fun, but I have work tomorrow, see ya later, buds...")
                self.current_state = self.sleep
            elif hour == 23:
                print("I know I said I'll go to sleep but have you seen this comic?")
                self.current_state = self.chat
            else:
                print("I love dnd")

    @prime
    def _work(self):
        while True:

            hour = yield

            if random() == 1:
                print("FINALLY, work is done, holidays are on")
                self.current_state = self.holidays
                break
            elif hour == 13:
                print("The lecture was tiring... Gotta go eat now")
                self.current_state = self.eat
            elif hour == 15:
                print("Heh, that cat pic is really cute...")
                self.current_state = self.chat
            elif hour == 18:
                print("I love dnd")
                self.current_state = self.play
            else:
                print("Stay focused, stay focused, stay focused...")

    @prime
    def _chat(self):
        while True:

            hour = yield
            if random() == 1:
                print("FINALLY, work is done, holidays are on")
                self.current_state = self.holidays
                break
            elif random() >= 0.6 and hour == 0:
                print("That was a fun chat, but I gotta go, sleep tight")
                self.current_state = self.sleep
            elif hour == 16:
                print("Deadines aren't waiting, sorry dear")
                self.current_state = self.work
            elif hour == 18:
                print("We've chatted, now let's go play some dnd")
                self.current_state = self.play
            else:
                print("Yeah, so about that movie you saw...")

def life_cycle(values):
    """Main func to the life cycle"""
    evaluator = FSM()
    for hour in values:
        evaluator.send(hour)
    return evaluator.does_match()

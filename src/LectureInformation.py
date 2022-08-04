from ProfessorInformation import ProfessorInformation

class LectureInformation:
    def __init__(self,name,time,credits,location,professor_name,professor_contact,rate_task,rate_mid,rate_final):
        self.name = name
        self.time = time
        self.credits = credits
        self.location = location
        self.rate_task = rate_task
        self.rate_mid = rate_mid
        self.rate_final = rate_final
        self.professorInformation = ProfessorInformation(professor_name,professor_contact)

    def setName(self,name):
        self.name = name

    def setTime(self,time):
        self.time = time

    def setLocation(self,location):
        self.location = location

    def setProfessorName(self,name):
        self.professorInformation.updateName(name)

    def setProfessorContact(self,contact):
        self.professorInformation.updateContact(contact)

    def setRateTask(self,rate):
        self.rate_task = rate

    def setRateMid(self,rate):
        self.rate_mid = rate

    def setRateFinal(self,rate):
        self.rate_final = rate

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getCredits(self):
        return self.credits

    def getLocation(self):
        return self.location

    def getProfessorName(self):
        return self.professorInformation.getName()

    def getProfessorContact(self):
        return self.professorInformation.getContact()

    def getRateTask(self):
        return self.rate_task

    def getRateMid(self):
        return self.rate_mid

    def getRateFinal(self):
        return self.rate_final
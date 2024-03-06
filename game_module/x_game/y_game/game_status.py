class GameStatus:
    def __init__(self) -> None:
        self.score=0
        self.playerDied=False
        self .isRunning=True
    def increase(self):
        self.score+=1
        
    def getPlayerDied(self):
        self.playerDied=True
    def getScore(self):
        
        return self.score
    def reset(self):
        self.playerDied=False
        self.score=0
    
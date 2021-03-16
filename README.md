# swg_game
It is a Snake water gun game written in python.
Its a single player game where user has to choose between snake, gun or water.
Use cases:

    ADMIN              USER               WINNER
    Water              Gun                Admin   
    Water              Snake              Admin
    Gun                Water              User
    Gun                Snake              Admin
    Snake              Water              User
    Snake              Gun                User
    Snake              Snake              None
    Water              Water              None
    Gun                Gun                None
    
I have used random module to choose the random response for the admin.    
For each win scores will be added to the scoreboard.
Then After 5 rounds the Result would be declared.

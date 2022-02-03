Player will be on the left side of the screen
To move up or down, you will need to use "W" for up and "S" for down.
The bot player moves slightly slower than the ball speed so that scoring is possible. 


here are the known bugs that I spotted during the development that I could not be bothered to fix:
* Player can move off the screen (not sure why you would want to do this intentionally. I could restrict movement, but that is not the objective of this project).
* Holding W or S will slow game speeds due to repetetive key presses (movement is already very fast, so no need to hold the keys down. Fixing this was not essential to the project so I did not add this into the code).
* Ball moves past the paddle in some rare scenarios even though it should reflect the ball (not sure the cause of this at the moment, likely caused by my algarithm checks).
* Changing to a fullscreen is possible, but the aspect ratio of the game remains the same and the ball bounces off invisible walls. Don't change resolution and it will work.
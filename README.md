# graverobber
### Python + HTML5/JS implementation of the game Graverobber, as it appears in the webseries Petscop. 
### See: [Graverobber](https://petscop.fandom.com/wiki/Graverobber/). 

###### This is just the game/rules library.



TODO:

- [ ] Needs a test suite, etc.
- [ ] Needs the recording feature implemented. *(by making 4 Plane objects and then two are for recording)*
- [ ] Needs a server that handles player sessions, etc.

Once all that's set up:
  - Set up the board.
  - Implement: The obstacle placing phase.
  - Implement: The grave placing phase.
  - Implement: The movement/digging phase.
  


**To interact with the boards all the API user does is declare their moves to the library, 
Adds them to a list of moves and sends the moves to the boards, which play out the moves autonomously.**

That way, the complexity of tracking which pieces are where is handled the natural way:
  - By setting up two boards with different conditions and then letting the system play out the same moves on them.
  - All the main loop of the game program has to really handle is telling the player if their move is invalid, taking turns, checking if someone has won yet, and displaying any flavor text or chat messages.

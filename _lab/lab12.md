---
layout: lab
num: lab12
ready: true
desc: "Battleship"
assigned: 2019-01-15 16:00:00.00
due: 2019-03-01 17:00
csxx: cs20
---

Note: this is not an auto-graded assignment.  We may still put it on Gradescope so that you can submit it there,
but there won't be any automated feedback.

<div>
    <h1><strong>Battleship! </strong></h1>
    <strong>Assignment Summary:</strong> Battleship is a children’s game where
    players guess (x,y) coordinate positions of the opposing player’s ship
    pieces in a 10x10 grid. For the official Hasbro rules and additional game
    context, read <a href="http://www.hasbro.com/common/instruct/Battleship.PDF">http://www.hasbro.com/common/instruct/Battleship.PDF<span
        style="color: black;"></span></a>
    . You will implement a version of this game in Python.<br>
    <br>
    <strong>* It is highly recommended that you read the entire assignment first
      to get an idea of what the end-goals are, which will help in designing
      your code.</strong><br>
    <br>
    This assignment is divided into five required stages and optional sixth
    stage. Each succeeding stage is built upon what you have already written for
    the previous stage. We expect you to design, write, and test this program
    according to these stages—first get the first-stage program working, then
    modify it to satisfy the second stage, and so on. As always, be sure to keep
    a copy of each completed stage. That way, if you decide you've gotten off on
    the wrong track for a stage, you can start again easily from the end of the
    previous stage, without the painstaking task of removing each addition. You
    should make sure that each stage is entirely correct and working perfectly
    before you go on to the next. As you complete each stage, you should
    demonstrate briefly to your TA or tutor that it works correctly before you
    go on to the following stage.<br>
    <br>
    Development by stages is good software engineering practice. It is far
    better to have a program that is correct but incomplete (i.e., it doesn't
    implement all the features but what it does implement is correct) than one
    that contains bugs. Grading for this assignment will reflect this, too; it
    will hurt your score much more to turn in buggy code than not to reach some
    of the later stages. Let's say that again: Your score will be higher if you
    do the first few stages correctly than if you do all of them with bugs in
    them.<br>
    <br>
    <strong>What to turn in:</strong>&nbsp;On Checkmate, a single Python file (<span
      style="font-family: monospace;">battleship.py</span>)
    containing your last-stage code. Do not turn in code from the optional Stage
    VI section.<br>
    <br>
     <strong>Grading:</strong>&nbsp;Your grade depends on organized development
    (did you design and debug each stage in sequence), completeness (does your
    program do everything the specification requires), correctness (does it
    produce the correct results), quality and clarity of your output, good
    modularity, good data organization (using data structures appropriately),
    and good programming style (are your identifier names descriptive, is your
    organization clear). You will receive appropriate partial credit for each
    stage you complete correctly. You will receive no credit for work on a later
    stage if the previous stages are incomplete or incorrect. The whole point of
    incremental development (i.e., stages) is to keep a programmer from biting
    off more than he or she can chew. <br>
    <br>
    <h2><strong><em>Rules</em><br>
      </strong></h2>
    The rules to implement will be largely based on the rules described here: <a
      href="http://www.hasbro.com/common/instruct/Battleship.PDF">http://www.hasbro.com/common/instruct/Battleship.PDF</a><br>
    <br>
    To summarize, the game consists of two players, Player 1 and Player 2. Each
    player will have 5 ship pieces of varying lengths (i.e. number of
    coordinates that it will occupy). Their names, identifying keys, and length
    are:  <br>
    <br>
    <span style="font-family: monospace;">Carrier (CAR)&nbsp;&nbsp;&nbsp; – 5
      coordinates<br>
       Battleship (BAT) – 4 coordinates<br>
      Cruiser (CRU)&nbsp;&nbsp;&nbsp; – 3 coordinates<br>
      Submarine (SUB)&nbsp; – 3 coordinates<br>
      Destroyer (DES)&nbsp; – 2 coordinates</span><br>
    <br>
    Each player will place their ships on a 10x10 grid where the columns are
    labeled 0 – 9 and the rows are labeled A – J (note, the column values are
    different than the ones listed in Hasbro’s official rules). The players will
    have their own space (i.e. player 1 and player 2 ships <strong>do not
      occupy the same grid</strong> - each player will have their own grid
    space). This grid organization is shown below:<br>
    <br>
    <span style="font-family: monospace;"> &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp;
      3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp; 7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _</span><br>
    <br>
    When a player places their ship pieces on the board, the entire piece must
    be within the board and each piece cannot overlap (you cannot have two ships
    occupying the same position). The player must place each ship vertically or
    horizontally on the grid (not diagonally). <br>
    <br>
    Each player will be unaware of the opposing player’s ship placement, and the
    objective of the game is to try and guess the ship positions the opposing
    player’s ships. Each player takes turns guessing the coordinates (Player 1
    starts the game), and the first player to guess all of the opposing player’s
    ship coordinates wins the game.<br>
    <br>
    When a player guesses the coordinate that an opposing player's ship
    occupies, then this counts as a “hit.” When a player guesses a coordinate
    that an opposing player's ship does not occupy, then this counts as a
    "miss." When a player guesses all coordinates of an opposing player's ship,
    then the ship is “sunk.” The game is over when a player sinks all of the
    opposing player’s ships.<br>
    <br>
    The players will need to maintain two views: an <strong>ocean view</strong>
    representing the player’s current ship placement and a <strong>target view</strong>
    representing the current player’s knowledge of the opposing player’s ship
    placement.   In addition to the views, each player must keep track of
    certain statistics and game state. These are:<br>
    <br>
    <strong>  Statistics</strong> (for each player): <br>
    &nbsp;&nbsp;&nbsp; - Number of moves made. <br>
    &nbsp;&nbsp;&nbsp; - Number of “hits” (correct guesses of the opposing
    player’s ship positions). <br>
    &nbsp;&nbsp;&nbsp; - Number of “misses” (incorrect guesses of the opposing
    player’s ship positions).  <br>
    <br>
    <strong>Game State</strong> (for each player): <br>
    &nbsp;&nbsp;&nbsp; - Both target and ocean view for each player.<br>
    &nbsp;&nbsp;&nbsp; - Each player's ship information (for each ship)
    including:<br>
    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; - A list of coordinate positions it
    occupies on its player's ocean view.<br>
    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; - The ships "health" (i.e. the number
    of coordinates that have not been hit).<br>
    <br>
    <h2><em><strong>Stage I – Setup</strong></em></h2>
    <p>For the first stage, it’s important that we lay out all the components
      that will be used throughout the game. The first thing that we will need
      to do is create the game board and lay out the ship pieces for each player
      before the game starts.</p>
    When designing an application, it’s important to think of what data
    structures should be used to represent the information of the program.
    Making decisions like this becomes easier with practice, but there are two
    things to keep in mind. First, start with the simplest data structure that
    does the job. (For example, you can consider creating a namedtuple
    representing a Ship that contains a list of coordinates that it occupies. Or
    perhaps you can consider using a set of coordinates instead of a list of
    coordinates). Second, accept that your first choice may not be your final
    choice; as the specifications become clearer or as circumstances change (or
    as you get to later stages in a problem like this one), you may decide that
    something else would work better. This kind of revision is a normal part of
    programming. It's no tragedy to rewrite or refactor some code in a better
    way, just as you should expect to revise written documents.<br>
    <br>
    Remember, one of the challenges (and most interesting thing) about coding is
    there are many ways to solve a problem. Most of the decisions should be made
    by you and your partner. However, some design guidance you can consider:<br>
    <ul>
      <li>Representing a 10x10 Grid can easily be done using 2D lists. Also,
        recall that lists (and 2D lists) are mutable, so assigning and replacing
        values in a 2D list is time / memory efficient.</li>
      <li>Each player will need to keep track of their views (both target and
        ocean) and Ship information.</li>
      <ul>
        <li>For the views, there are many ways to organize this. Following the
          examples in lecture, you can create a separate 2D list for each view
          for each player (four 2D lists total).</li>
        <li>For the ships, the most important pieces of information are the
          ships name (displayed when the ship gets hit or sunk), the ship's
          current health (there are other ways to derive this information, but
          it would be nice to keep track of and instantly access this), the list
          of coordinates that the ship occupies in its respective player's ocean
          view (which can be a set of strings representing specific
          coordinates). </li>
        <li>Each player will need to create ships, which will be updated
          throughout the game. Since each player only has one ship of each type
          (and each have a unique identifying key), you can organize these ships
          in a dictionary for each player: The key in the dictionary will be the
          three-character ship string (stated in the rules), and the value in
          the dictionary will be the corresponding Ship namedtuple.</li>
        <li>Throughout gameplay, you will need to reference both views (to see
          if moves are valid and what ship information / statistics needs to be
          updated), and the Ship's state (checking if a ship occupies a
          coordinate and updating the Ship's state accordingly).</li>
      </ul>
      <li>Each player will also need to keep track of game statistics.</li>
      <ul>
        <li>The requirements are to keep track of three pieces of information
          for each player: number of moves made, number of hits, and number of
          misses. Similar to a ship's state, a dictionary can be used to map
          these three statistics (perhaps using keys like "moves", 'hits",
          "misses") and their corresponding int values.</li>
        <li>This information will be used to display a summary of statistics
          when the game ends.</li>
      </ul>
    </ul>
    For now, users can interact with our game via the Python shell (though a
    user would probably prefer to interact with a graphical interface). Each
    player will need to define their ships’ positions, and though one approach
    to do so can be interactive, we will require each player to store their ship
    configurations in a text file (<strong>“p1.txt”</strong> for Player 1’s ship
    placement and <strong>“p2.txt”</strong> for Player 2’s ship placement). An
    example input file for <strong>p1.txt</strong> can look like this:<br>
    <br>
    <span style="font-family: monospace;"> CAR,A1,A2,A3,A4,A5<br>
      BAT,B1,B2,B3,B4<br>
      CRU,C1,C2,C3<br>
      SUB,D1,D2,D3<br>
      DES,E1,E2</span><br>
    <br>
    An example input file for <strong>p2.txt</strong> can look like this:<br>
    <span style="font-family: monospace;"><br>
      CRU,A3,B3,C3<br>
      BAT,A2,B2,C2,D2<br>
      DES,A5,B5<br>
      CAR,A1,B1,C1,D1,E1<br>
      SUB,A4,B4,C4</span><br>
    <br>
    Each line in the file represents a specific ship with a three-character key
    (for example, Carrier is represented as “CAR”) as shown in the previous
    Rules section.&nbsp; A line will also contain a list of coordinates it
    occupies. Each piece of information is separated by ‘,’ and the number of
    coordinates is dependent on the type of ship. There are certain things your
    program should check for when loading the files:<br>
    <ul>
      <li>The user can input their ships in any order and your program will need
        to check and make sure the file is correct including:</li>
      <ul>
        <li>Each distinct ship has the correct length.</li>
        <li>Each ship is laid out horizontally or vertically.</li>
      </ul>
      <ul>
        <li>Ship coordinates do not overlap with each other.</li>
      </ul>
      <ul>
        <li>The coordinates themselves are valid positions (there shouldn't be
          invalid coordinates like <span style="font-family: monospace;">“Z3”</span>).</li>
      </ul>
      <ul>
        <li>The ship keys are valid (it will either be <span style="font-family: monospace;">‘CAR’,
            ‘BAT’, ‘CRU’, ‘SUB’, ‘DES’</span>.)</li>
      </ul>
      <ul>
        <li>There are no duplicate ships in the file (a particular ship’s
          configuration cannot appear more than once).</li>
      </ul>
    </ul>
    If any of these conditions are not met, the program will print out a short
    statement stating there was a problem with reading the file and then the
    program will terminate.<br>
    <br>
    As you are parsing through the player ship configuration files, it’s
    important to organize your information into the appropriate data structures.
    For example, in addition to modifying the player’s ocean view, you will need
    probably need to store the coordinates and initial ship state such as
    current health (or number of coordinates that have not been hit), the name
    of the ship, the ships coordinates, etc. Again, this is largely dependent on
    the decisions of what data type you want to use in order to represent /
    organize data to solve problems effectively.<br>
    <br>
    You will need to print out the board showing the current state of the game.
    A few notes about displaying the board:<br>
    <ul>
      <li>The board should be populated with underscores “_” for each position
        by default (an empty board example is shown in the previous Rules
        section).</li>
      <li>For the ocean view, if a ship occupies a certain coordinate, then an
        asterisk “*” is displayed.</li>
      <li>Throughout the game, the ocean view will change since when a player
        guesses a coordinate that a ship occupies, this asterisk should change
        to “X”. This is for the player whose ship was just hit. The target view
        for the player making the guess will need to be changed (as described
        below).</li>
      <ul>
        <li>At the end of the game, a losing player’s ocean view will have all
          “*” replaced by “X”.</li>
        <li>The ocean view does not change for misses (i.e. only coordinates
          occupied by a ship should be replaced with an "X" if a hit occurs. The
          "_" characters remain unchanged if a miss happens.</li>
      </ul>
      <li>Initially, for the target view, since a player has not fired yet, the
        board should be populated with only underscore characters.</li>
      <ul>
        <li>Throughout the game, the player's target view will change since when
          a player guesses a coordinate that the opposing player ship occupies,
          then the “_” will be replaced with a “H”, which represents a hit for
          that position.</li>
        <li>When a player guesses a coordinate that the opposing player ship
          does not occupy, then the “_” will be replaced with an “M”, which
          represents a miss for that position.</li>
      </ul>
    </ul>
    At this stage, we shouldn’t worry about changing the target view and we
    should only worry about populating the player’s ocean view based on the
    input file. However, you should create functions that can print out any
    player’s ocean or target view in a nice tabular format as shown above.<br>
    <br>
    Using the sample p1.txt file above, Player 1’s initial ocean view (when
    printed out nicely) will look like:<br>
    <br>
    <span style="font-family: monospace;">  &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp;
      3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp; 7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _</span><br>
    <br>
    <h2><em>Stage II – User Input and the Game Loop</em></h2>
    <p>For this stage, the main goal is to have the program interact with the
      user. Since we want to make this game somewhat user-friendly, we will
      accept both lower-case and upper-case commands from the user. Before the
      game starts, prompt the user if they would like to start a new game or
      quit the program. A sample title menu will look like this:</p>
    <span style="font-family: monospace;">--------- BATTLESHIP! ---------<br>
      <br>
      N:&nbsp;&nbsp;&nbsp; New Game<br>
      Q:&nbsp;&nbsp;&nbsp; Quit<br>
      Enter command:</span><br>
    <br>
     When the user enters “Q” (or “q”), then the application will terminate. If
    the user enters “N”, then the program will read both “<strong>p1.txt</strong>”
    and “<strong>p2.txt</strong>” (both of these files will be placed in your
    program’s working directory) and populate each ocean view as discussed in
    Stage I.<br>
    <br>
    If all is well, then the game can officially start where Player 1 makes the
    first guess. At the start of each turn, the output should indicate which
    player’s turn it is, the current player’s target view, the current health
    for each players’ ships (each player will need to display their health in a
    tabular two-column format), and a player turn menu prompting the player to
    enter their next move. The options for the user that the user can choose
    from are printing out their current ocean view or firing at a specific
    opposing player’s coordinate. <br>
    <br>
    A few notes about printing out a player’s ocean view:<br>
    <ul>
      <li>During gameplay, the opposing player will need to be honorable and
        look away if the opposing player is looking at the screen while their
        ocean view is displayed - this knowledge will clearly be unfair.</li>
      <li>Printing out the ocean view isn’t really necessary for gameplay since
        a player won’t need to refer to their ocean view for anything besides
        book keeping (and we're implementing our program to take care of this
        for us).</li>
      <li>We present the option to the user to print their ocean view and it
        will also be useful for testing your code.</li>
    </ul>
    If the player chooses to fire at the opposing player’s position, then the
    program will prompt the player to enter the coordinates. This will need to
    be in the form of [A-J][0-9]. Your program must check if the coordinate is
    valid, and if it is, that the player has not already fired at that specific
    position. If the player has already guessed a specific coordinate (which
    should already appear as either an “M” or “H” on the player’s target view),
    then the program should allow the user to continue entering a coordinate
    until one is valid.  <br>
    <br>
    One thing you will need to solve is 2D list indexing will not recognize the
    characters A through J as a valid position. You can write a helper function
    that takes in a character A – J and returns the appropriate index to access
    the 2D list (for example, A = 0, B = 1, C = 2, etc.). You probably have not
    seen the function <span style="font-family: monospace;">ord</span> (short
    for “ordinal”) yet that takes in a single character and returns the numeric
    representation of that character (recall, in class we talked about how each
    character has a value associated with it and that’s how we can sort
    strings). Also recall that characters have incremental values associated
    with it, so B = A + 1, C = A + 2, D = A + 3, etc. Consider having a function
    that takes in a character and subtracts the ordinal value from ‘A’ to get
    the 0-based index for the 2D list. For example <span style="font-family: monospace;">print(ord('B')
      – ord('A'))</span> should print 1.<br>
    <br>
    With all that said, here is a sample output of what the user interaction
    will look like at this stage (note, the bold text indicates user input):<br>
    <br>
    <span style="font-family: monospace;">--------- BATTLESHIP! ---------<br>
      <br>
      N:&nbsp;&nbsp;&nbsp; New Game<br>
      Q:&nbsp;&nbsp;&nbsp; Quit<br>
      Enter command: <strong>N</strong><br>
      <br>
      Player 1's Turn<br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      Player 1 Ships HP&nbsp;&nbsp; Player 2 Ships HP<br>
      CAR -
      5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CAR - 5<br>
      BAT -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      BAT - 4<br>
      CRU -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CRU - 3<br>
      SUB -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      SUB - 3<br>
      DES -
      2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      DES - 2<br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>I</strong><br>
      Invalid command: Please re-enter command. <strong>O</strong><br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>F</strong><br>
      Enter target's coordinate [A-J][0-9] to fire at: <strong>fjksal</strong><br>
      Invalid coordinate. Please enter coordinate [A-J][0-9]: <strong>Z1</strong><br>
      Invalid coordinate: Please enter coordinate [A-J][0-9]: <strong>A2</strong><br>
      Battleship hit!<br>
      <br>
      Player 2's Turn<br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      Player 1 Ships HP&nbsp;&nbsp; Player 2 Ships HP<br>
      CAR -
      5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CAR - 5<br>
      BAT -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      BAT - 3<br>
      CRU -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CRU - 3<br>
      SUB -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      SUB - 3<br>
      DES -
      2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      DES - 2<br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>O</strong><br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; *&nbsp; X&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>F</strong><br>
      Enter target's coordinate [A-J][0-9] to fire at: <strong>A1</strong><br>
      Carrier hit!<br>
      <br>
      Player 1's Turn<br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; _&nbsp; H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      Player 1 Ships HP&nbsp;&nbsp; Player 2 Ships HP<br>
      CAR -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CAR - 5<br>
      BAT -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      BAT - 3<br>
      CRU -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CRU - 3<br>
      SUB -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      SUB - 3<br>
      DES -
      2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      DES - 2<br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>F</strong><br>
      Enter target's coordinate [A-J][0-9] to fire at: <strong>A2</strong><br>
      Please enter another coordinate [A-J][0-9]: <strong>A3</strong><br>
      Cruiser hit!<br>
      <br>
      Player 2's Turn<br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      Player 1 Ships HP&nbsp;&nbsp; Player 2 Ships HP<br>
      CAR -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CAR - 5<br>
      BAT -
      4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      BAT - 3<br>
      CRU -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CRU - 2<br>
      SUB -
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      SUB - 3<br>
      DES -
      2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      DES - 2<br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command: <strong>O</strong><br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; *&nbsp; X&nbsp; X&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; *&nbsp; *&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; *&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; *&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      Enter command:</span><br>
    <br>
    <h2><em>Stage III – Saving State </em></h2>
    At this point, your program should be able to load players’ ship
    configuration files, run the game loop (including prompting the user for
    input, interpreting that input, modifying the application data, can display
    the players’ Target and Ocean views, and displays the current health for
    each player’s ships for every turn).<br>
    <br>
    It’s not unreasonable to have the players play an entire game of Battleship,
    but it would be nice to allow the players to save their game and resume it
    at a later point. In this stage, you will need to implement functionality to
    write game data to a file (known as “serializing” the data), read game data
    from a file into the program and resume gameplay.<br>
    <br>
    Note, there are many ways one can serialize data. However, for this
    assignment, your file will need to write and read game state data to a file
    named “<strong>game.txt</strong>” with the following format:<br>
    <br>
    ----- # start of file (not actually part of file content) ----<br>
    <span style="font-family: monospace;">A1<br>
      <br>
      B2<br>
      A1,A2,A3,A4,A5,B1,B3,B4,C1,C2,C3,D1,D2,D3,E1,E2<br>
      CRU,3,C1,C2,C3<br>
      BAT,4,B1,B2,B3,B4<br>
      SUB,3,D1,D2,D3<br>
      DES,2,E1,E2<br>
      CAR,5,A1,A2,A3,A4,A5<br>
      1,1,0<br>
      B2<br>
      <br>
      A1<br>
      A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,D1,D2,E1<br>
      CRU,3,A3,B3,C3<br>
      BAT,4,A2,B2,C2,D2<br>
      SUB,3,A4,B4,C4<br>
      DES,2,A5,B5<br>
      CAR,4,A1,B1,C1,D1,E1<br>
      1,1,0<br>
      P1</span><br>
    ---- # end of file (not actually part of file content) ----<br>
    <br>
    Each line is described as:<br>
    <ul>
      <li>Line1: Coordinates that were “hits” in Player 1’s target view
        separated by ‘,’</li>
      <li>Line2: Coordinates that were “misses” in Player 1’s target view
        separated by ‘,’</li>
      <li>Line3: Coordinates that were “hits” in Player 1’s ocean view separated
        by ‘,’</li>
      <li>Line4: Ship coordinates that were not hit yet in Player 1’s ocean view
        separated by ‘,’</li>
      <li>Line5 – 9: Player 1’s Ship information. Each line represents a single
        ship. There are several important pieces of information that we need to
        save for each ship. The format that is used is:<br>
        [three-character key for ship],[ship health], [coordinates of ship
        separated by ‘,’]. Note, the order of the ships do not matter (i.e. BAT
        can be listed before DES and DES can be listed before BAT).</li>
      <li>Line10: Player 1 statistics in the following format:
        [moves],[hits],[misses]</li>
      <li>Line11 – 20: The same information as described for Lines 1 – 10, but
        this information is specific to Player 2.</li>
      <li>Line21: A string that’s either “P1” or “P2” representing if it’s
        Player 1’s or Player 2’s turn respectively.</li>
    </ul>
    Besides the functionality for writing, reading, and loading game state, we
    will need to provide the Player an option to load a game when the program
    starts (in the Title Menu) and an option to save a game during a player’s
    turn. For example, you will need to change and support a Title Menu with the
    following options:<br>
    <br>
    <span style="font-family: monospace;">--------- BATTLESHIP! ---------<br>
      <br>
      L:&nbsp;&nbsp; &nbsp;Load Game (game.txt)<br>
      N:&nbsp;&nbsp; &nbsp;New Game<br>
      Q:&nbsp;&nbsp; &nbsp;Quit</span><br>
    <br>
    and a Turn Menu with the following options:<br>
    <br>
    <span style="font-family: monospace;">O: Print Ocean View<br>
      F: Fire at player<br>
      S: Save Game</span><br>
    <br>
    Note that the game should continue resuming if the player chooses to save
    the game. All this does is write the game state to a file called “<strong>game.txt</strong>”
    and resumes the game.<br>
    <br>
    <h2><em>Stage IV - End Game: Displaying Game Statistics</em></h2>
    <p>At this point, most of the heavy lifting is done and we have a fairly
      complete game. The last thing to worry about is displaying the game
      statistics. Throughout Stage II, you should be keeping track of each
      players’ statistics (moves made, hits made, misses made).</p>
    <p>When a player wins the game, the program should state so and player
      statistics throughout the game should be displayed in a two-column fashion
      (similar to displaying each player’s ships’ health for each turn). After
      the statistics are displayed, the application should terminate. The
      statistics that need to be displayed for each player are:</p>
    <ul>
      <li>Number of moves made throughout the game.</li>
      <li>Number of misses the player made.</li>
      <li>Number of hits the player made.</li>
      <li>The hit percentage (with 3 decimal precision)</li>
      <li>The miss percentage (with 3 decimal precision)</li>
    </ul>
    An example of Player 1 making the last move to win the game and displaying
    the statistics:<br>
    <br>
    <span style="font-family: monospace;">Player 1's Turn<br>
      &nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp;
      7&nbsp; 8&nbsp; 9<br>
      A&nbsp; _&nbsp; H&nbsp; H&nbsp; H&nbsp; H&nbsp; H&nbsp; M&nbsp; _&nbsp;
      _&nbsp; _ <br>
      B&nbsp; _&nbsp; H&nbsp; H&nbsp; H&nbsp; H&nbsp; H&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      C&nbsp; _&nbsp; H&nbsp; H&nbsp; H&nbsp; H&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      D&nbsp; _&nbsp; H&nbsp; H&nbsp; M&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      E&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      F&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      G&nbsp; M&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      H&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      I&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      J&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp; _&nbsp;
      _&nbsp; _ <br>
      <br>
      Player 1 Ships HP&nbsp;&nbsp; Player 2 Ships HP<br>
      CAR -
      0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CAR - 1<br>
      BAT -
      0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      BAT - 0<br>
      CRU -
      0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      CRU - 0<br>
      SUB -
      0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      SUB - 0<br>
      DES -
      2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      DES - 0<br>
      <br>
      O: Print Ocean View<br>
      F: Fire at player<br>
      S: Save Game<br>
      Enter command: <strong>F</strong><br>
      Enter target's coordinate [A-J][0-9] to fire at: <strong>E1</strong><br>
      Carrier hit!<br>
      You have sunk the enemey's Carrier<br>
      Player 1 wins!<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Player 1
      Stats&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Player 2 Stats<br>
      Moves:&nbsp;
      20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      19<br>
      Misses:
      3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      4<br>
      Hits:&nbsp;&nbsp;
      17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      15<br>
      Hit%:&nbsp;&nbsp;
      85.000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      78.947&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <br>Miss%:&nbsp;
      15.000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      21.053&nbsp; <br>
    </span><br>
    <h2><em>Stage V – Cleaning Up Your Code</em></h2>
    <p>At this point, all of the functional requirements should be satisfied,
      but maybe the code you wrote is disorganized, inefficient, duplicate code
      exists in various places, information you included that isn’t necessary to
      have, etc. That doesn't mean you shouldn't test your code until this
      stage, each stage should be tested in tandem to implementation. However,
      at this point, the entire game functionality is done and there may be
      design decisions that made sense for a particular stage, but now that your
      code is working end-to-end, there is always room for cleanup. For example,
      reading ship information from the player ship configuration file and
      reading ship information from game.txt have similar functionality. Check
      and see if you're re-writing the same code for this and think if you can
      reduce duplicate code and generalize this functionality such that the same
      code can be used for both parts of the program. Part of what we grade you
      on is quality of your code. This stage should be dedicated to reviewing
      your current version and see if there are ways to make it more organized,
      elegant, and efficient.</p>
    <p><br>
    </p>
    <h2><em>Stage VI (optional) – Improvements and Extensions</em></h2>
    <p>For those of you who have finished early, feel free to use the remaining
      time to improve your program. This is completely optional and you will not
      receive extra credit for completing it. I encourage everyone to attempt
      some of this just for practice. It’s completely up to you, so feel free to
      be as creative as you like. Some things you can consider working on:</p>
    <h3></h3>
    <strong>Improving the User Experience</strong> – There are several
    improvements that you can make in your application.<br>
    <ul>
      <li>We required the player’s to provide a text file with the initial
        ship’s coordinates. You can attempt to make this process more
        interactive by prompting the players to manually enter the coordinates
        for each of their ships. Or maybe you want to write the functionality
        for ships to be placed randomly instead of the user providing ship
        configuration files.</li>
      <li>The flow of commands can be more robust. For example, once the player
        enters the command to fire, there isn’t an option for the player to
        return back to the Turn Menu (and the player’s only choice is to enter a
        coordinate to fire at). Though this is minor, improving the flow of user
        interaction can be worked on.</li>
    </ul>
    <strong>Modifying the Game</strong> – We’ve implemented the traditional
    version of battleship, however there can be many different ways you can
    modify this game (for better or worse). Some ideas that may spark your
    imagination:<br>
    <ul>
      <li>The ships are set on the game board and do not move throughout the
        game. What if the ships can move one space after every player’s turn (or
        every other turn)? There are some mechanics you will need to take into
        account. For example, if two ships are moving and are about to collide,
        then who gets priority? Also, will the ships only move in one direction,
        and if so, will they circle around to the other end of the board? The
        concepts of hits / misses on the board may not apply for these modified
        rules.</li>
      <li>Perhaps having a player make one move every turn gets boring after
        some time. What if each ship has a certain speed attribute and a player
        can fire multiple times at the opposing player before they can fire
        back?</li>
    </ul>
    <strong>Adding Additional Statistics</strong> – We needed to do some
    bookkeeping for simple statistics throughout the game. However, there are
    many other things that could be important to keep track of (dedicated
    business teams are always trying to gather information to make the best
    possible decisions for the future of a product). For example, maybe keeping
    track of a hit / miss streak for each player is something that might be of
    interest. <br>
    <br>
    ... or anything else you think would be good to work on. Again, this part is
    totally optional and students can be really creative here. What you work on
    is up to you, so go nuts!<br>
    <br>
    <h3><em>Tips and Advice</em></h3>
    <ul>
      <li>Take time to draw out and design your code! Don't start coding
        immediately until you know the overall organization and structure of the
        components you want to implement. This will significantly help you
        during implementation.</li>
      <li>Get started early! There are a lot of parts to this lab and additions
        to make for each stage. You will need ample time to complete this
        assignment and will most likely require you to get started early
        (including finding a partner on Monday and utilizing all lab sections).</li>
      <li>Save multiple versions of your project! Since each stage builds upon
        each other, you may make changes that can break your current
        functionality. In the worst-case scenario, you made modifications in
        your file, broke the code, and now nothing works. By saving several
        versions of your progress, you can always start from a later point
        rather than trying to start all over.</li>
      <li>Create game.txt versions (or be sure to save versions for specific
        scenarios) that allow you to test various cases. For example, if you’re
        working on confirming the functionality for the end-of-game (printing
        stats, checking logic, etc.), it will be extremely annoying to replay an
        entire game just to get to that point. Imagine trying to debug an edge
        case at the end of the game and having to start a new game, hit all
        player ships just to reproduce the condition, realize the bug is still
        not fixed, and then replaying the game again… it will be wise to play
        with the game once, load a game.txt file as discussed in Stage III that
        has a near-complete game, and then testing the end-game conditions.</li>
    </ul>
    <hr>
    <p><font face="Helvetica" size="1"><font face="Helvetica" size="1"><font face="Helvetica"
            size="1"><font
              face="Helvetica"
              size="1"><font
                face="Helvetica"
                size="1"><font
                  face="Helvetica"
                  size="1"><font
                    face="Helvetica"
                    size="1"><font
                      face="Helvetica"
                      size="1">Written
                      by Richert Wang in Spring 2016. Based on David G. Kay's
                      Anteater Bed and Breakfast assignment in Winter 2016.<br>
                    </font></font></font></font></font></font></font></font></p>
    <ul>
    </ul>
</div>

Summary/Information on various on the following projects


**************************
NOTE: The listed projects were initially part of 
MIT's Introduction to Computational Thinking and Data Science.
The problems/challenges were posed by MIT,
and I went ahead and attempted to solve them.
**************************


Simulation Of Viruses
Algorithms With Cows
Robot Vaccuums





*******************

Algorithms With Cows

*******************

NOTE: For this program to work you must have the cow_data.txt and partitions.py file to run it properly.
The .txt file contains data about the different cows (the name and weight) and partitions.py file creates all
the possible ways to carry the cows for the brute force program to search through.

The objective of this object was to create two programs to transport cows over space in a ship in the most efficient way 
possible, find the optimal way to transport cows and compare the efficiencies of both.

I made a program utilized the greedy algorithm.

In brief, the greedy algorithm seeks out the most optimal option (or node/vertex on a graph) among its neighbours 
(current options) and travels to it, then seeks out the most optimal option from that option and so on.

In this case, the greedy algorithm will try to find the heaviest group of cows that the ship can carry within a 
prescribed limit.

Then I made a program that used the brute force algorithm.

While the greedy algorithm tried to find the most optimal option among its current options, the brute force program will explore
every possible combination of carry sets of cows to determine the most optimal one. 

In the end, the brute force algorithm did find the optimal solution, while the greedy algorithm rarely did so.

However, the brute force program is extremely inefficient and not practical for industrial use.
The greedy algorithm, while very fast, is extremely unreliable for industrial use unless selecting optimal options
at all times always leads to optimal results. 

What did I learn?

I learned to how to program basic algorithms and read .txt files.

What's next?

I'd like to take a crack at programming the simplex algorithm, an algorithm that is 
used widely in the real world. I also first learned about it in CO 250 (intro to Optimization)
and would like to learn more. 


    
*******************

Vacuum Robots

*******************
The objective of this project is to run simulations of different type of vaccuum robots onto different types of rooms
and analyze the results.

To do this I had to create a Position class (functions like 'coordinates' except it can seek out its next position based
on type of robot), a Rectangular Room class, and a Robot class. From the Robot class, I made a Standard Robot class
(Robot moves in one direction until it hits a wall, then randomly selects a direction, other than its current direction,
a travel that way) and I made RandomWalk Robot Class (robot changes direction after each 'time-step').

Then I programmed a simulation that test these Robots and track how many time-steps it takes to clean a specificied
percentage of the room.

Standard Robots seem decent at vaccuuming rooms, Randomwalk robots are quite terribe (see for yourself by running some
simulations).

What I learned?
I practised more object oriented programming, I learned how to write simulations that track movement, and I learned
how to plot the results from the simulation. 
 
What's next?

I want to learn try to make a more efficient vaccuum Robot (in terms of # of time steps). 

I have attempted to make one, but my idea seemed unreasonable (it required the robot to travel to 
one end of the room...suppose it travelled to the 'bottom' of the room, it would clean the entire bottom row of floor
tiles, travel up one, then clean that entire row tiles and so on. For rectangular rooms, it might work, for anything
else, it might just explode.'). 

I also want to create non-rectangular rooms and make robots that can clean those.

*******************

Simulation of Viruses

*******************

The objective for this project is to simulate the effect of drugs (or lack thereof) on a Patient infected with
various viruses. 

To do this I had to create Patient,Virus and Drug classes and create Virus and Drug objects.

Then I programmed a simulation with a Simple (non-mutating, non-resistant) virus infected onto a Patient.

What you can do?

Run simulations with 2 types of basic viruses (non-mutating/non-resistant and a mutating/resitant virus) 
and their affect on a Patient with or without treatment(drugs).

What I might do?

If I ever read up on more diseases/viruses, I might add more virus types, I might add other disease classes (bacteria,
worms, fungi etc.) and/or make my objects more sophisticated and realistic.
  
What I gained from this project?

I got more experience with object oriented programming, creating simulations
and visualizing the simulations' results (with pylab).



  
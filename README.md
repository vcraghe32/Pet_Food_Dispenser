
# Pet Food Dispenser

**Note** - For more information about this project, please feel free to visit our [project GoogleDoc](https://docs.google.com/document/d/1ZKXdEp18WFhlqO-TDtYp-zZMlVuGLO5934JrBp6huCs/edit?usp=sharing). The project GoogleDoc contains inventory, idea brainstorms, schedule, cute pet pictures, and initial project ideas.
[project Whiteboard](https://www.whiteboard.chat/board/98881ae5-cb39-46fe-b3e7-05e48ab4fd4d-pgNum-1).
# Overview
After completing the basic OnShape and CircuitPython assignments, the next assignment was the first Engineering III 
project. The project did not have many constraints. Its main goal was to be a challenging project. No specific task was 
given, but the project had to make use of CircuitPython and CAD (Computer-Aided Design).

For the first Engineering III project, we (Violet Craghead-Way and Luke Frank) decided to create a pet food dispenser. 
Both having pets, a pet food dispenser sounded like an applicable and fun idea. There were not many constraints on 
this project. The main constraint was that the project had to be a challenge.

The tools that were used for this project are as follows:

* OnShape - OnShape was used for CAD. OnShape was helpful because it is a cloud-based program. 
  It automatically saves work to the cloud. Working on the cloud is a useful measure against data loss. 
  Unlike Solidworks, another CAD program, OnShape allows for collaboration at the same time.

* PyCharm - PyCharm was used for CircuitPython. PyCharm is useful in that it is compatible with GitHub 
  commits, pushes, and pulls. It also has spell checks, a built-in serial monitor, and can suggest code improvements.

* Caret - Similar to PyCharm, Caret was used for CircuitPython. Note that **Caret is for Chromebook.** PyCharm operates 
  only on Macs and PCs. For Chromebooks, Caret is a useful piece of software for programming in CircuitPython. It does 
  not have a built-in serial monitor, so the application **Beagle Term** (serial monitor) goes hand-in-hand with it.

### If it is helpful, here is the link to the T-Slot feature OnShape document: [T-Slot Link](https://cvilleschools.onshape.com/documents/5791a167e4b03c2aa6af3b35/w/8528f1c2d733302d4632f38e/e/7eab6eb8ff7dea85b9cc6a87)

# The Problem And Goal 

Dealing with hungry pets is frustrating. Whether it is the mournful meow of a cat, or the piercing puppy eyes of a 
dog, hungry pets can be both distracting and irritating. We each have two pets 
(a dog and cat for Luke and two dogs for Violet), so we understand the struggle.

Luckily, with a pet food dispenser, meal time for pets can be made into a more entertaining and enjoyable experience. 
Pets would no longer come pleading to humans for their food because their food source would be in one place. 
Additionally, an automated pet food dispenser would give pets a concrete sense of a meal time schedule 
which would be hard to rival when done by humans. 

# Brainstorm

### Archimedes Screw
![Pet Food Dispenser Archimedes Screw Design](./Media/Pet_Food_Dispenser-Archimedes_Screw_Design_Idea.JPG.jpg)

The brainstorm began with the idea of an Archimedes screw. The basic components of the design were an Archimedes screw, 
rotated by a continuous rotation servo and a hole-shaped dispensing area for pouring the food into. 
Additionally, the rate by which food was supplied to a pet would be determined by the speed of the continuous-rotation 
servo. Finally, the design included an inclined plane for the food to travel on after being transported by the 
Archimedes screw. The inclined plane would lead to a pet food bowl or to a space where the pet could eat the food.

**Note - citation for the website where the image was taken from:** 
Kristina Panos, et al. “Dual Pet Food Dispenser Is Doubly Convenient.” Hackaday, 31 May 2015, hackaday.com/2015/05/31/dual-pet-food-dispenser-is-doubly-convenient/. 

**EasyBib was used for generating the MLA citation.**

However, the Archimedes screw design was rejected because of its inconvenience in laser cutting. The screw would have 
required an inefficiently large amount of 3D printing. The alternative to 3D printing was to develop a 2D design that 
could expand, but a 2D expandable design was determined to be unideal and unnecessarily complicated.

### Two Gears 
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Two_Gears_Design_Brainstorm.JPG" width="450"><img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Two_Gears_Design_Full_View.JPG.jpg" width="400">

Our second idea was to have two gears: one with a hole that would create a pathway when aligned with the hole on the 
wall, and another that would be attached to that gear and the 180 servo. The wheel would turn 90 degrees, stay for 
a few seconds to dispense the right amount, and then go back to its original position covering the hole. 

However, this design was flawed in that food pellets could be crushed when the wheel rotated. Additionally, the weight 
put on the servo would have been very heavy, considering the weight of the pet food. Because of these reasons, 
the design seemed flawed, so we brainstormed again.

### Water Wheel
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Food_Wheel_Design_Brainstorm.JPG" width="450">

Our final brainstorm idea that we will be using is a water-wheel like design that will dispense pet food pellets 
instead of water. The food flows into the small containers inside the food wheel, and then moves in a circular motion. 
The pull of gravity and the push of a continuous rotation servo turn the continuous rotation servo, and the food pellets 
drop when the container faces downwards. The food is contained by rubber hinge flaps while it is being filled up to keep 
the small containers in the food wheel closed. When the wheel does a complete rotation a certain quantity of food is 
dispensed, so it is easy to measure and provide serving sizes. In addition, when the food drops from the small 
containers into the box, an inclined plane will bring the food down to the bowl. 

## Design Versions 

### Version 1
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Food_Wheel_Design_Planning.JPG" width="400">

These are the measurements for the first(current) versions of our water wheel, hinge 
(for opening the battery holder/food container), and funnel walls. The water wheel design has worked so far, however the 
funnel design was difficult  to mate together in OnShape, so we decided to create a box with a  3D design insert that 
would act as inclined planes around the hole of the box so that the food moves down to the water wheel. 

# Schedule 

| Date: | Goal: |
| --- | --- |
| As of 1/13/21: | A design idea for CAD involving a food wheel, funnel, and slide. |
| 1/27/21 | A draft of what the 3D design will be. It does not have to be created in OnShape, but there should be a plan for how the design will be made. |
| 2/10/21: | A rough draft of 3D design on OnShape. The funnel, wheel, and slide are assembled in a way that they would be able to work together. Additionally, a rough draft of the code. |
| 2/17/21: | A revised draft of the 3D design on OnShape, as well as the code. |
| 2/24/21: | Another revised 3D design on OnShape. Ideally, the this or the previous design can be tested in the Sigma Lab. If it does not work, then one final 3D design will be created. |
| 3/1/21: | The final 3D design on OnShape. |

# OnShape Document:

Here is the link to the OnShape document: 
[OnShape Document](https://cvilleschools.onshape.com/documents/015179800deb9471f00f5f8e/w/bea41924170b278a6561fb34/e/8fa549fe2ac3d84aadd2efb3)

This OnShape document will contain the CAD for our project. 

# Lessons Learned
  Be sure to assemble the correct version of the part that you will be using in real life. I made the mistake of assembling everyhing with the standard servo arm and base instead of the microservo arm and base.

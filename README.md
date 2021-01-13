
# Pet Food Dispenser

[Project GoogleDoc](https://docs.google.com/document/d/1ZKXdEp18WFhlqO-TDtYp-zZMlVuGLO5934JrBp6huCs/edit?usp=sharing) contains: inventory, idea brainstorms, schedule, cute pet pictures, and initial project ideas.

# Overview
After completing the basic OnShape and CircuitPython assignments, the next assignment was the first Engineering III project. The project did not have many constraints. Its main goal was to be a challenging project. No specific task was given, but the project had to make use of CircuitPython and CAD (Computer-Aided Design).

For the first Engineering III project, we (Violet Craghead-Way and Luke Frank) decided to create a pet food dispenser. Both having pets, a pet food dispenser sounded like an applicable and fun idea. There were not many constraints on this project. The main constraint was that the project had to be a challenge.

The tools that were used for this project are as follows:

* OnShape - OnShape was used for CAD. OnShape was helpful because it is a cloud-based program. It automatically saves work to the cloud. Working on the cloud is a useful measure against data loss. Unlike Solidworks, another CAD program, OnShape allows for collaboration at the same time.

* PyCharm - PyCharm was used for CircuitPython. PyCharm is useful in that it is compatible with GitHub commits, pushes, and pulls. It also has spell checks, a built-in serial monitor, and can suggest code improvements.

* Caret - Similar to PyCharm, Caret was used for CircuitPython. Note that **Caret is for Chromebook.** PyCharm operates only on Macs and PCs. For Chromebooks, Caret is a useful piece of software for programming in CircuitPython. It does not have a built-in serial monitor, so the application **Beagle Term** (serial monitor) goes hand-in-hand with it.

# The Problem And Goal 

Dealing with hungry pets is frustrating. Whether it is the mournful meow of a cat or the piercing puppy eyes of a dog, hungry pets can be both distracting and irritating. We each have two pets (a dog and cat for Luke and two dogs for Violet), so we understand the struggle.

Luckily, with a pet food dispenser, meal time for pets can be made into a more entertaining and enjoyable experience. Pets would no loner come pleading to humans for food because their food source would be in one place. Additionally, an automated pet food dispsenser would give pets a concrete sense of a meal time schedule which would be hard to rival when done by humans. 

## Brainstorm

### Archimedes Screw
![Pet Food Dispenser Archimdes Screw Design](./Media/Pet_Food_Dispenser-Archimedes_Screw_Design_Idea.JPG.jpg)

Initially, the plan was to create a horizontally-shaped pet food dispenser that utilized an Archimedes screw design. The basic components of the design would be as follows:

* An Archimedes screw, rotated by a continuous rotation servo.

* A hole-shaped dispensing area for pouring the food into. The rate by which food was supplied to a pet would be determined by the speed of the continuous-rotation servo.

* An inclined plane for the food to travel on after being transported by the Archimedes screw. The inclined plane would lead to a pet food bowl or to a space where the pet could eat the food.

Here is a picture of the Archimedes screw design:

**Note - citation for the website where the image was taken from:** 
Kristina Panos, et al. “Dual Pet Food Dispenser Is Doubly Convenient.” Hackaday, 31 May 2015, hackaday.com/2015/05/31/dual-pet-food-dispenser-is-doubly-convenient/. 

**EasyBib was used for generating the MLA citation.**

The Archimedes screw design was rejected because of its inconvenience in laser cutting. The scew would have used much 3D printing reasources, so the alternative was to develop a 2D design that could expand. It was unideal. 
### Two Gears 
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Two_Gears_Design_Brainstorm.JPG" width="450"><img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Two_Gears_Design_Full_View.JPG.jpg" width="400">

Our second idea was to have two gears: one with a hole that would create a pathway when aligned with the hole on the wall, and another that would be attached to that gear and the 180 servo. The wheel would turn 90 degrees, stay for a few seconds to dispense the right amount, and then go back to its original position covering the hole. This design would easily crush the food pellets, and the weight put on the servo would be very heavy considering the weight of the pet food. Because of these reasons, we brainstormed again.
### Water Wheel
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Food_Wheel_Design_Brainstorm.JPG" width="450">

Our final brainstorm idea that we will be using is a water-wheel like design that will dispense pet food instead of water. The food flows into the small containers inside the food wheel, and then moves in a circular motion with the pull of gravity and the push of a continuous rotation servo, and drops when the container faces downwards. The food is contained by rubber hinge flaps while it is being filled up to keep the small containers in the food wheel closed. When the wheel does a complete rotation a certain quanity of food is dispensed, so it is easy to measure and provide serving sizes. In addition, when the food drops from the small containers into the box, an inclined plane will bring the food down to the bowl. 
## Design Versions 
### Version 1
<img src="https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/Media/Pet_Food_Dispenser-Food_Wheel_Design_Planning.JPG" width="400">

These are the measurments for the first(current) versions of our water wheel, hinge(for opening the battery holder/food container), and funnel walls. The water wheel design has worked so far, however the funnel design was difficult  to mate together in OnShape so we decided to create a box with a  3D design insert that would act as inclined planes around the hole of the box so that the food moves down to the water wheel. 

Here is the link to the OnShape document: 
[OnShape Document](https://cvilleschools.onshape.com/documents/015179800deb9471f00f5f8e/w/bea41924170b278a6561fb34/e/8fa549fe2ac3d84aadd2efb3)

# Lessons Learned
Work in progress...

# C4D-Frontal-to-UVW-Utility
## A Python Script which emulates Camera Projection

- CinemaUVWThingy.py -> The Python Script
- CinemaUVWThingyWithMainObject -> A variation from the original Script with a material container container Object
- ThingyTest.mp4 -> A example Video
- ThingyTest.c4d -> A example Cinema4d Project


Script works as Python Script Tag

It detects all Objects in the Scene which have "ax_" in their name.

The variation also detects the Object with "axmain_" in its name and uses it to retrieve the material.

It then automatically refreshes the UVW tag every frame.

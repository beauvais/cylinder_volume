cylinder_volume
===============

## A quick script for finding the volume of a cylinder.

The volume of a cylinder is found by multiplying its height by the radius of its circular aspect, represented as the formula:

v = hπr<sup>2</sup>

If the unit of measurement is centimetres, this formula would give you the number of cubic centimetres (*cc<sup>3</sup>*) it contains. In SI, 1 cm<sup>3</sup> is equal to .001l (so 1000 cm<sup>3</sup> is 1l).



### find_volume

The function *find_volume* takes two arguments: *height* and *radius* as numbers (integers or floats) of centimetres equal to the height and radius of the cylinder. 

This script returns the number of ccm<sup>3</sup>s in the cylinder as the variable *v*, and the number of litres in the variable *litres*.

### print steps

Through *find_volume* there are print() functions which are commented out. If a result does not look right, or in the case of an error, these will print each step in the process to show where the error might be.

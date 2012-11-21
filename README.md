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


## TODO

The reason for this script was to find the volume (in litres) of a stainless steel pot from its listed dimensions in centimetres. This is to find a large enough brew kettle.

Several things that this script could become:

* A larger package for identifying more specific home brewing elements:
    * litres to pints
    * loss of volume through evaporation
    * size of pot to match target brew
    * size of kegs
    * number of bottles
        * sizes of bottles (volume)
        * number of bottlecaps (in bags)
* A web application which takes requirements for a brew, and builds essential parts based on the requirements (with optionals)
* Combined with a scraper or similar price-watching app which could alert when an item matching the scripts options comes online for sale:
    * creates search terms:
        * if boiler:
            search = ["stock pot", "stainless steel stock pot", "brew kettle"]
            search_sizes = [cylinder_volume + " litres", height + (radius*2)]
    * searches amazon, ebay, and other sites accepting search terms
    * returns matching URIs for listings and prices
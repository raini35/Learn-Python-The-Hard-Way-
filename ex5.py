programmer_name = 'Rainier Go' 
current_age = 35
height_now = 74
weight_now = 180
conversion_in_to_cm = 2.54
conversion_lb_to_kg = 0.453592
height_in_cm = height_now * conversion_in_to_cm 
weight_in_kg = weight_now * conversion_lb_to_kg
eye_color = 'Brown' 
teeth_color = 'Semi-White'
hair_color = 'Brown' 

print "Let's talk about %s." % programmer_name 
print "He's %d inches tall." % height_now 
print "He's %d pound heavy." % weight_now 
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (eye_color, hair_color) 
print "His teeth are usually %s depending on the coffee." %teeth_color

print "If I add %d, %d, and %d I get %d." % ( current_age, height_now, weight_now, current_age 
+ height_now + weight_now) 

print "This is my height in centimeters. %d " % height_in_cm
print "This is my weight in kilograms. %d" % weight_in_kg
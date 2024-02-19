# The script of the game goes in this file

### Characters ####################################
# Narrator won't be declared, its simply the default speaker.
define who = Character("????")
define snail = Character("Friendly Snail")
define huck = Character("Huck")

### ### Character Images ############################
###### Main Character Images ##############
image MC Neutral = "images/characters/main character/MC neutral.png"

###### Huck Images ###############
image Huck Neutral = "images/characters/huck/huck_neutral.png"


### Backgrounds ############################
image bg Black = "images/backgrounds/bgBlack.png"
image bg White = "images/backgrounds/bgWhite.png"
image bg storybook_1 = Movie(play="images/backgrounds/storybook/Storybook1.webm")
image bg storybook_2 = Movie(play="images/backgrounds/storybook/Storybook2.webm")
image bg storybook_3 = Movie(play="images/backgrounds/storybook/Storybook3.webm")
image bg storybook_4 = Movie(play="images/backgrounds/storybook/Storybook4.webm")
image bg storybook_5 = Movie(play="images/backgrounds/storybook/Storybook5.webm")
image bg storybook_6 = Movie(play="images/backgrounds/storybook/Storybook6.webm", image="images/backgrounds/bgWhite.png",loop=False)
image bg Cave_A1 = "images/Backgrounds/cave_a1.png"
image bg Cave_A2 = "images/Backgrounds/cave_a2.png"
image bg Cave_A3 = "images/Backgrounds/cave_a3.png"
image bg Cave_A4 = "images/Backgrounds/cave_a4.png"
image bg Camp = "images/Backgrounds/bg camp.png"
image bg Class Select = "images/backgrounds/classSelect.png"


# The game starts here.

label start:

    ### Starting Variables
    default playerClass = 0 ## this is used to figure out which class the character is.
                            ## 1 is the Fighter
                            ## 2 is the Mage
                            ## 3 is the Bard
    ###### Inventory Items (This is so items, after being collected, don't show up again)
    ######### Escape the Hole ###################
    default small_bars = False
    default large_bars = False
    default rope = False

    ###### Room Visits (These are for if the player has been to this section before. This will prevent repeating certain dialogue)
    default caveA1_visit = False

    scene black
    with dissolve

    $ renpy.pause(1.0)

    "Did you know magic exists?"

    show bg storybook_1 
    with dissolve

    "It comes from the blooming flowers."
    "It hums with the whistling grass."
    
    show bg storybook_3
    with dissolve

    "It flows in the rivers."
    "It floats on the breeze."

    show bg storybook_2
    with dissolve

    "It comes from sparkling gemstones, deep underground."
    "It is small and fleeting..."

    show bg storybook_4
    with dissolve

    "...like the bugs who learned to harness it."
    "Legend says, there is a source of magic more powerful than anything found in the woods."

    show bg storybook_5
    with dissolve

    "A Shooting Star."
    "It is said that Shooting Stars that land in the forest have the ability to grant wishes."
    "Any wish one can think of can come true as long as they have a Star."

    show bg Black
    with dissolve

    "But you have to be quick..."
    "Like all Stars, fallen ones disappear with the sun."

    show bg storybook_6
    with dissolve

    "When one lands, you only have until dawn to get to it."
    "And you may not be the only one racing to get to the Star..."
         
    scene black 
    with dissolve

    $ renpy.pause(1.0)

label cave_Area1:

    if caveA1_visit == True:
        jump cave_Area1_Loop
    else:
        who "You okay down there?"
        $ renpy.pause(0.5)
        who "Little One? You alright?"
        who "Hello?"

        show bg Cave_A1

        show MC Neutral at left
        
        with dissolve

        show Huck Neutral at right
        with dissolve

        snail "Can you fly out of there, Little One?"

        "You stretch out your wings and start to fly out of the hole."

        show MC Neutral at left
        with hpunch

        "You fall, hard. Glancing at your wing, you see it's torn."

        snail "Well, that's no good...."
        snail "Maybe look around for something to get out?"
        snail "Don't worry, I won't go anywhere."

        $ caveA1_visit = True

label cave_Area1_Loop:

        hide screen cave_a2_items
        hide screen cave_a3_items
        hide screen cave_a4_items

        scene bg Cave_A1
        with dissolve

        show screen cave_a1_nav
        with dissolve
        $ renpy.pause()

        jump cave_Area1_Loop

label cave_Area1_Check:

    show MC Neutral at left
    show Huck Neutral at right
    with dissolve

    if small_bars == True and large_bars == True and rope == True:
        snail "Everything you've gathered, it almost seems like..."
        snail "Yes! A ladder! All those supplies can build a ladder!"
        snail "Here, I'll guide you through the steps."
        jump escaped_hole
    else:
        snail "Have a look around. I'm sure there are useful items around here somewhere."
        snail "This looks like some kind of construction zone for a new outpost."
        snail "Perhaps there are some tools lying around?"
        jump cave_Area1_Loop

label cave_Area2:

    hide screen cave_a3_items
    hide screen cave_a4_items

    scene bg Cave_A2
    with dissolve

    if not small_bars:
        show screen cave_a2_items
        with dissolve

    show screen cave_a2_nav
    with dissolve
    
    $ renpy.pause()

    jump cave_Area2


label cave_Area2_Pickup:

    "You took quite the tumble on the way down."
    "It looks like this area is filled with the twigs you broke."

    jump cave_Area2

label cave_Area3:

    hide screen cave_a2_items
    hide screen cave_a4_items

    scene bg Cave_A3
    with dissolve

    if not large_bars:
        show screen cave_a3_items
        with dissolve

    show screen cave_a3_nav
    with dissolve

    $ renpy.pause()

    jump cave_Area3

label cave_Area3_Pickup:

    "These must be part of the construction the snail was talking about."
    "Hopefully the Construction Ants won't mind you borrowing these."

    jump cave_Area3

label cave_Area4:

    hide screen cave_a2_items
    hide screen cave_a3_items

    scene bg Cave_A4
    with dissolve

    if not rope:
        show screen cave_a4_items
        with dissolve

    show screen cave_a4_nav
    with dissolve

    $ renpy.pause()
    
    jump cave_Area4

label cave_Area4_Pickup:

    "Rope. You're sure rope can be helpful."
    "Rope is always helpful!"

    jump cave_Area4

label escaped_hole:

    scene black
    with dissolve

    "You quickly climb up the makeshift ladder. The friendly snail waits patiently, and even helps you out once you near the top."

    show bg Camp
    with dissolve

    show MC Neutral at left
    show Huck Neutral at right
    with dissolve

    "You shake yourself off."

    show MC Neutral at left 
    with hpunch

    "Right... your wing."
    "It really hurts."
    "You gently lift your wing to take a good look at it."

    snail "That doesn't look good..."
    snail "Let me set up camp and we'll tend to that."

    scene bg Black
    with dissolve

    "Time Skip~~~~~~~~"

    show bg Camp
    show MC Neutral at left
    show Huck Neutral at right
    with hpunch

    "You fall back as a Field Mouse jumps out of the woods, between you and the snail."
    "It must have been attracted to the smell of the food."

    snail "A MOUSE!!!"
    snail "Quick, run to the Outpost! We'll be safe there!"

    hide Huck with hpunch

    "You rush to try and get to the snail but the mouse rushes towards you, sending you crashing into some of the snail's leftover supplies."

    hide MC with dissolve

    show bg Class Select
    with dissolve
    
    "In front of you lies a pin blade, a jasper staff, and a spider-string harp."
    "You need to protect yourself."

label selectClass:

    scene bg Class Select

    show screen itemSelect

    $ renpy.pause()

    jump selectClass

label sword_selected:

    "You'll cut the mouse down to size!"
    

    jump end

label staff_selected:

    "You picked the staff!"
    "[playerClass]"

    jump end

label harp_selected:

    "You picked the harp!"
    "[playerClass]"

    jump end


label end:
    # This ends the game.
    window auto
    "GAME OVER"
    return

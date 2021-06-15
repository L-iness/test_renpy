# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define menu = nvl_menu

define s = Character('Sylvie', kind=nvl, color="#c8ffc8")
define m = Character('Me', kind=nvl, color="#c8c8ff")


image s = "e_normal.png"
image uni = "bg uni.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene uni

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s
    with dissolve

    # These display lines of dialogue.

    s "You've created a new Ren'Py game."

    s "Once you add a story, pictures, and music, you can release it to the world!"


    menu (nvl=True):
        m "Let's test it then!"

        "Now":
            jump now

        "Not now":
            scene black
            with dissolve
            "{b}Bad Ending{/b}."
            return


label now :
    show s
    with dissolve

    s "Ok! Let's start!"

    nvl clear

    scene black
    with dissolve

    "{b}Starting...{/b}."

    "I'll ask her..."

    nvl clear

    m "Um... will you..."
    m "Will you be my artist for a visual novel?"

    nvl clear

    "Silence."
    "She is shocked, and then..."

    s "Sure, but what is a \"visual novel?\""

    nvl clear

    scene black
    with dissolve

    "{b}Good Ending{/b}."


    # This ends the game.

    return

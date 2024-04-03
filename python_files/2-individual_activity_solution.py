"""
The local college planned a day at the park with different activities, people, and food.
You were tasked to find people who wanted to participate in these activities. You make sure
to mention that if they do come, they'll get free food. When the time came to start the picnic
however, it's a mess. People don't show up, activities don't go to plan, and you need to think
of a solution fast. 

You need to find a way to use ALL the default set methods found in the lesson in order to complete the exercise.

Time limit: 1 hour
"""
# A Chaotic College Picnic

def main():
    # Participant set
    participants = {"Bob", "Megan", "Lucas", "George", "Stephanie", "Marcy", "Mike", "Jace"}

    # Attending activity sets
    face_painting_participants = {"Bob", "Mike", "Stephanie", "Marcy"}
    corn_hole_participants = {"Jace", "Megan"}
    kickball_participants = {"Bob", "Megan", "Lucas", "George", "Stephanie", "Marcy", "Mike", "Jace"}
    bouncy_house_participants = set() # Alternative way of making a set

    """
    Problem 1: Mike realizes that no one has signed up
    to use bouncy house and decides to be the first.
    """

    # Add Mike as a bouncy house participant. 
    bouncy_house_participants.add("Mike")

    """
    Problem 2: While playing corn hole, Jace and Megan
    hear Mike yell to them to jump with him. They couldn't
    say no. They join him. You need to remove them from the corn
    hole activity and add them to the bouncy house activity.
    """
    # Combine the corn hole participants with the bouncy
    # house participants
    bouncy_house_participants = bouncy_house_participants | corn_hole_participants

    # OR bouncy_house_participants = bouncy_house_participants.unison(corn_hole_participants)

    # Remove Jace and Megan from the corn hole activity
    corn_hole_participants.remove("Jace")
    corn_hole_participants.remove("Megan")
    
    """
    Problem 3: Bob didn't show up to the picnic.
    You remove his name from the roster.
    """
    # Remove Bob's name from all sets using .remove()
    face_painting_participants.remove("Bob")
    kickball_participants.remove("Bob")
    participants.remove("Bob")

    """
    Problem 4: Bob was supposed to bring the face paint, but he
    didn't show up. You started the kickball game early because
    of it. After the picnic was over, you text Bob, wondering
    where he was. You need to find the participants that wanted
    to face paint and apologize for Bob's absence.
    """
    # Intersect (or find the common participants between) the master
    # participant and the face paint list to find the participants
    # you need to apologize to. Remove each from the face painting
    # roster
    owe_an_apology = participants & face_painting_participants

    # OR owe_an_apology = participants.intersection(face_painting_participants) 
    
    # for every person you owe an apology to
    for sad_participant in owe_an_apology:
        
        # Remove each participant from the roster
        face_painting_participants.remove(sad_participant)
        
        # *optional: Apologize to the sad face painters
        print(f"I'm sorry {sad_participant}, but Bob never showed up with the face paint.")
        

    # Print Results
    print(f"Face Painting Participants: {face_painting_participants}")
    print()
    print(f"Participants: {participants}")
    print(f"Corn Hole Participants: {corn_hole_participants}")
    print(f"Kickball Participants: {kickball_participants}")
    print(f"Bouncy House Participants: {bouncy_house_participants}")

if __name__ == "__main__":
    main()
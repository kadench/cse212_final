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

    # Implement the solution for problem 2 here.
    
    # Expected Result:
    # Bouncy House Participants: {'Mike'}

    """
    Problem 2: While playing corn hole, Jace and Megan
    hear Mike yell to them to jump with him. They couldn't
    say no. They join him. You need to remove them from the corn
    hole activity and add them to the bouncy house activity.
    """
    
    # Implement the solution for problem 2 here.

    # Expected Result:
    # Bouncy House Participants: {'Jace', 'Megan', 'Mike'}
    # Corn Hole Participants: set()

    
    """
    Problem 3: Bob didn't show up to the picnic.
    You remove his name from the roster.
    """

    # Implement the solution for problem 3 here.

    # Expected Result: Bob doesn't exist in any set.

    """
    Problem 4: Bob was supposed to bring the face paint, but he
    didn't show up. You started the kickball game early because
    of it. After the picnic was over, you text Bob, wondering
    where he was. You need to find the participants that wanted
    to face paint, remove them from that activity, and apologize
    for Bob's absence.
    """

    # Implement the solution for problem 4 here.
    
    # Expected Result:
    # Participants: {'George', 'Lucas', 'Stephanie', 'Mike', 'Marcy', 'Megan', 'Jace'}
    # I'm sorry Marcy, but Bob never showed up with the face paint.
    # I'm sorry Stephanie, but Bob never showed up with the face paint.
    # I'm sorry Mike, but Bob never showed up with the face paint.
    # Face Painting Participants: set()

    # Print Results
    print(f"Face Painting Participants: {face_painting_participants}")
    print()
    print(f"Participants: {participants}")
    print(f"Corn Hole Participants: {corn_hole_participants}")
    print(f"Kickball Participants: {kickball_participants}")
    print(f"Bouncy House Participants: {bouncy_house_participants}")

if __name__ == "__main__":
    main()
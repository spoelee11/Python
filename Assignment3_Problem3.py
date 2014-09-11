# Tyson Spoelma
# Homework 3
# Problem 3

# This program keeps track of a network of people and their likes
network = {}

response = ''
while(response != 'Q'):
    print "Enter a person in the network, or hit Q to quit: "

    response = raw_input()
    if (response == 'Q'):
        print 'Here are is the network: '
        print network
        print "\nQuitting..."
        exit
    else:
        print "Enter in a space-separated list of people this person likes: "
        likeString = raw_input()
        likes = likeString.split()
        print likes
        if (response in network):
            network[response].append(likes)
            # print network[response]
        else:
            network[response] = likes

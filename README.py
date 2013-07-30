Opening-Closing-Files
=====================
# main function opens and reads presidents file then uses that info to create two new files.
def main():
    #open's presidents file and save's it to a varibale to be used for other files
    inputF = open('presidents.txt.', 'r')
    line = inputF.readline()
    inputF2 = open('presidents2.txt', 'r')
    #creates a new file to be writen too
    outfile = open('same_order.txt.', 'w')
    #creates a new file to be writen too
    outfile2 = open('last_name.txt.', 'w')
    # turns file into list to be tinketered with
    lastName = inputF2.readlines()
    #sorts list
    lastName.sort()
    # switch first and last name, place formats and completes list into sentances.
    for n in lastName:
        sent = n.split('\t')
        lead = sent[0:2]
        del sent[0:2]
        for q in lead:
            format(q)
            sent.insert(0, q +' ')
        sent.insert(2, ' was president from ')
        sent.insert(4, ' to ')
        
        for i in sent:
            format(i)
            outfile2.write('%4s' % i)
                   
    #loop to go through each line of president's file and apply output function to it creating first list.        
    while line:
        output(line, outfile)
        line = inputF.readline()

#close files
    inputF.close()
    inputF2.close()
    outfile.close()
    outfile2.close()
    
#create output function 
def output(line, outfile):
    #break each line to pieces that can be rearranged
    sentance = line.split('\t')
    a = sentance[0]
    b = sentance[1]
    c = sentance[2]
    d = sentance[3]
    #sort the line's how they should be.
    outfile.write(b +' '+ a+ ' was president from '+ c+' to '+ d + '\n')

main()

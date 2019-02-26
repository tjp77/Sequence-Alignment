#!/user/bin/python
import sys;




def ReadInSequences():
    
    sequence1 = " ";
    sequence2 = " "; 
    
    try:
        
        file = open("sequenceData.txt", "r");
        
        sequence1 = file.readline().strip(); 
        sequence2 = file.readline().strip(); 
        
    except:
        
        print("Trouble reading input file 'sequenceData.txt'. Make sure file exists and is in correct format."); 
        print("Input format may be incorrect. Refer to documentation for correct format.");
        sys.exit(0);
    
    else:
        
        print("\nsequenceData.txt read successfully.\n");
    
    file.close();
    retVal = [sequence1, sequence2];
    return retVal;





def Main():
    
    sequences = ReadInSequences();
    
    
    
    return 0;





Main();







# ----- Notes / ToDo -----

"""

Use sequences from in class expamples in the sim file for testing since know they exact result/output. 









"""

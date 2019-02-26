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
    retVal = (sequence1, sequence2);
    return retVal;


def PrintMatrixToFile(matrix):
    
    fileName = input("\nEnter a name for the alignment matrix file:\n");
    fileName = fileName + ".txt";
    notSaved = True;
    
    while (notSaved)
    try:
        
        file = open(fileName, "w");
        
        # Finish matrix output. 
        # Print one row per line. 
        # Maybe print sequence lables as top row/ first char of each column.
        
    except:
        
        print("Could not write to file 'sequenceData.txt'. Please do nit include file extension/type in the entered name. "); 
        
    else:
        
        print("\nMatrix save successful.\n");
        notSaved = False;
    
    file.close();
    
    return 0;


def CreateMatrix(sequence1, sequence 2):
    
    # populate first row and column as required. 
    
    # Fill in the rest with one of the 3||4 choices based on algorithm type. 
    
    return 0;


def TraceBack(matrix):
    
    
    return 0;


def Main():
    
    sequences = ReadInSequences();
    
    
    
    return 0;





Main();







# ----- Notes / ToDo -----

"""

Use sequences from in class expamples in the sim file for testing since know their exact result/output. 

"Genomic data you will use for your project should be retrieved from Genbank" - Then change to this. 


[] Finish Alignment/matrix fill funtion. 

[] Rename alignment function to which ever version we end up using for clarification.

[] Finish print matrix to file func. Give user the option after the matrix creation to do the saving of the file for inspection.

[] How to find/track mutations? 

----------------------------------------------------------------------------------------------------------------------------------------------------

To complete the project, you need:

1)     Understand Genbank entries at NCBI and answer the following questions for “https://www.ncbi.nlm.nih.gov/assembly/GCF_000928555.1”:

i)       What’s the size/length of this flu virus genome? What is it made of? (RNA/DNA)?

ii)     How many genes does this virus genome contain; what are their names?

iii)   What does CDS mean? How many CDSs are there? How many proteins does the virus genome code? What are they?


2)     Implement pairwise alignment in python (or whatever language your group likes) (you group should figure out which alignment algorithm you need to use);

3)     Pairwise align a sequence of “NP” gene with another “NP” gene, for example NC_026429.1 vs EF554797.1 (these two are links on project page);

4)     Count the number of mutations and characterize each mutation. So you should have two tables like [see project page].






"""

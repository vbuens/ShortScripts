from __future__ import division
import sys
import os
import argparse

#  DISCLAIMER: Needs to modify the Structure_syn_all_data_biallelic to remove the _1 and _2 from the file in order to be read
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', type=str, default='Structure_syn_all_data_biallelic.txt', required= True, help='Structure file to find markers')
    parser.add_argument('-l', '--samplesfile', type=str, help='File with a list of samples and the group they belong to')
    parser.add_argument('-p', '--percentage', type=int, help='Percentage of missing data accepted. Example: 10 (%)')
    args = parser.parse_args()
    libfile = args.samplesfile
    inputfile = args.inputfile
    perc = args.percentage

    return inputfile,libfiles,perc

def main(inputfile,libfiles,perc):
    outputfile = open('NORemoving_errors/markers_Filtered_'+str(perc)[2:]+'.txt', 'w')
    #outputfile_51 = open('markers_group51_'+str(perc)[2:]+'.txt', 'w')
    #outputfile_1 = open('markers_group1_'+str(perc)[2:]+'.txt', 'w')
    outputfile2 = open('NORemoving_errors/AllMarkers'+str(perc)[2:]+'.txt', 'w')

    Pop1 = []
    Pop2 = []
    Pop3 = []
    Pop4 = []
    Pop51 = []

    # Add each samples into their populatio n list
    for line in libfile:
        bits = line.split()
        if bits[1]== '1':
            Pop1.append(str(bits[0]))
        if bits[1]== '2':
            Pop2.append(str(bits[0]))
        if bits[1]== '3':
            Pop3.append(str(bits[0]))
        if bits[1]== '4':
            Pop4.append(str(bits[0]))
        if bits[1]== '51':
            Pop51.append(str(bits[0]))

    # Bases that all samples from a certain population have for each marker
    Pop1_pos = []
    Pop2_pos = []
    Pop3_pos = []
    Pop4_pos = []
    Pop51_pos = []


    outputfile2.write ('group'+ '\t' + 'markers'+ '\t'+ str(Pop1) + '\t'+ str(Pop2) + '\t'+ str(Pop3) +'\t'+ str(Pop4) + '\t'+ str(Pop51) +'\n') #+'\t'+ str(Pop51)
    # Write heading of output file:
    outputfile.write('Marker'+ '\t' + 'Pop1'+ '\t' + 'Pop3'+ '\t'+ 'Pop4'+ '\t'+ 'Pop41'+ '\t'+ 'Pop46'+'\t'+ 'Pop51' + '\n') #+ '\t'+ 'Pop7'+'\t'+ 'Pop0ld' '\n') # ('group'+ '\t' + 'markers'+ '\t'+ str(Pop1) + '\t'+ str(Pop2) + '\t'+ str(Pop3) +'\t'+ str(Pop4) + '\t'+ str(Pop41)+'\t'+ str(Pop46) +'\t'+ str(Pop51)+'\n')

    firstline = inputfile.readline() # read first line with library names
    bits = firstline.split() # split first line so I have each library as an array element

    # for each population, go through all the libraries in it, and save the position of the library
    for i in Pop1:
        indices = [j for j, x in enumerate(bits) if x == i]
        Pop1_pos.append(indices)
    for i in Pop2:
        indices = [j for j, x in enumerate(bits) if x == i]
        Pop2_pos.append(indices)
    for i in Pop3:
        indices = [j for j, x in enumerate(bits) if x == i]
        Pop3_pos.append(indices)
    for i in Pop4:
        indices = [j for j, x in enumerate(bits) if x == i]
        Pop4_pos.append(indices)
    for i in Pop51:
        indices = [j for j, x in enumerate(bits) if x == i]
        Pop51_pos.append(indices)

    print(f'Printing pop1_pos:\n{Pop1_pos}')

    # Go through the input file again, and get the SNP bases for each marker for every population.
    # If there is is missing data, add to the count

    for line in inputfile:
        # Get each one of the markers (get each line and split it into array elements)
        bits = line.split()

        Pop1_Snp = [] ;    Pop2_Snp = [] ;    Pop3_Snp = [];     Pop4_Snp = [];    Pop51_Snp = [];  #  Pop46_Snp = []      #Pop51_Snp = []
        count_1=0;    count_2=0;    count_3=0;    count_4=0;    count_51=0;    #count_46=0      #count_51=0

        # Get the SNP bases for each marker
        for i in range(int(len(Pop1_pos))):
            num=bits[int(Pop1_pos[i][0])]+bits[int(Pop1_pos[i][1])]
            if num != '-9-9':
                Pop1_Snp.append(num)
            else:
                count_1+=1

        for i in range(int(len(Pop2_pos))):
            num=bits[int(Pop2_pos[i][0])]+bits[int(Pop2_pos[i][1])]
            if num != '-9-9':
                Pop2_Snp.append(num)
            else:
                count_2+=1

        for i in range(int(len(Pop3_pos))):
            num=bits[int(Pop3_pos[i][0])]+bits[int(Pop3_pos[i][1])]
            if num != '-9-9':
                Pop3_Snp.append(num)
            else:
                count_3+=1

        for i in range(int(len(Pop4_pos))):
            num=bits[int(Pop4_pos[i][0])]+bits[int(Pop4_pos[i][1])]
            if num != '-9-9':
                Pop4_Snp.append(num)
            else:
                count_4+=1

        for i in range(int(len(Pop51_pos))):
            num=bits[int(Pop51_pos[i][0])]+bits[int(Pop51_pos[i][1])]
            if num != '-9-9':
                Pop51_Snp.append(num)
            else:
                count_51+=1

        #Checking the percentage of missing data - accept a certain % of missing data (variable: perc)
        #  If all the groups have less missing data than permited, continue. Otherwise, finish.
        if float(count_1/len(Pop1_pos)) < perc and float(count_2/len(Pop2_pos)) <perc and float(count_3/len(Pop3_pos)) <perc and float(count_4/len(Pop4_pos))<perc and float(count_51/len(Pop51_pos)) <perc: # and float(count_46/len(Pop46_pos)) <0.9:     #and float(count_51/len(Pop51_pos)) <0.5

            Pop1_set=set(Pop1_Snp) ;        Pop2_set=set(Pop2_Snp);        Pop3_set=set(Pop3_Snp);        Pop4_set=set(Pop4_Snp);   #     Pop41_set=set(Pop41_Snp);
            Pop51_set=set(Pop51_Snp)


            rem=[]
            for i in Pop1_set:
                if ((Pop1_Snp.count(i)/len(Pop1_Snp))<perc_error):
                    rem.append(i)
            for i in rem:
                Pop1_set.remove(i)
           rem=[]    
           for i in Pop2_set:
               if ((Pop2_Snp.count(i)/len(Pop2_Snp))<perc_error):
                 rem.append(i)
           for i in rem:
               Pop2_set.remove(i)
            rem=[]
            for i in Pop3_set:
                if (Pop3_Snp.count(i)/len(Pop3_Snp)<perc_error):
                  rem.append(i)
            for i in rem:
                Pop3_set.remove(i)
            rem=[]
            for i in Pop4_set:
                if (Pop4_Snp.count(i)/len(Pop4_Snp)<perc_error):
                  rem.append(i)
            for i in rem:
                Pop4_set.remove(i)

            # If the SNP is consistent within a population:
            if len(Pop1_set) == 1 and len(Pop2_set) == 1 and len(Pop3_set) == 1 and len(Pop4_set) == 1 and len(Pop51_set) == 1: # and len(Pop46_set) == 1:

               counts+=1

    #            total=list(Pop1_set)+list(Pop2_set)+list(Pop3_set)+list(Pop4_set)+list(Pop51_set) #+list(Pop0_set)+list(Pop7_set)
                total=list(Pop1_set)+list(Pop3_set)+list(Pop4_set)+list(Pop51_set) #+list(Pop0_set)+list(Pop7_set)

                total_set=set(total)

                if len(total_set)>=2:
    ##                if Pop1_set==Pop
    ##                                   outputfile.write(str(bits[0]) + '\t'+ str(Pop1_Snp) +'\t'+ str(Pop2_Snp) + '\t'+ str(Pop3_Snp) +'\t'+ str(Pop4_Snp) +'\t'+ str(Pop41_Snp)+'\t'+ str(Pop46_Snp)+ '\n') #+ str(Pop51_Snp)+'\t'
    #                outputfile.write(str(bits[0]) + '\t'+ str(list(Pop1_set)[0]) +'\t'+ str(list(Pop2_set)[0]) + '\t'+ str(list(Pop3_set)[0]) +'\t'+ str(list(Pop4_set)[0]) +'\t'+ str(list(Pop51_set)[0]) + '\n' ) # +'\t'+ str(list(Pop7_set)[0]) +'\t'+ str(list(Pop0_set)[0])+'\n')
                    outputfile2.write(str(bits[0]) + '\t'+ str(list(Pop1_set)[0]) +'\t'+ str(list(Pop2_set)[0]) +'\t'+ str(list(Pop3_set)[0]) +'\t'+ str(list(Pop4_set)[0]) +'\t'+ str(list(Pop51_set)[0]) + '\n' ) # +'\t'+ str(list(Pop7_set)[0]) +'\t'+ str(list(Pop0_set)[0])+'\n')
#

    return




if __name__ == '__main__' :
    inputfile,libfiles = parse_arguments()
    main(inputfile,libfiles)

import os

path_data="../virus_sequence/" # data we download from NCBI
path_result="../1line_result/"       # result
name_of_file=os.listdir(path_data) # get all name of data_file
print(name_of_file)
special=['join','complement']  # for special elements, it is different from normal information of sequence
                                #so when we should develop another way to get accession_id from special sequence

for name in name_of_file:
    message = {} # we will use dictionary in python to ensure that for same accession, we will put their sequences together.
    file=open(path_data+name,encoding="utf-8")# we read the data
    save=open(path_result+name,"w")  #we will write our result in this file
    content=file.readline()
    sequences = ""
    accession = "" # accession_id

    while content:
        if ">" in content:
            # we will get accession from information line
            if special[0] not in content and special[1] not in content:
                accession = content.split('.')[0][1:]

            elif special[0] in content or special[1] in content and "complementary" not in content:
                accession = content.split('(')[1].split('.')[0]


        elif "\n" == content:
            # if we first time process this accession:
            if message.get(accession) is None:
                if accession!="":
                    message[accession] = sequences

            # if we second or more times process this accession:
            else:
                message[accession] = message[accession] + sequences # we connect the original sequences with new sequences
            content = file.readline()
            sequences = ""  #initialize
            accession = ""  #initialize
            continue
        else:
            sequences += content[:-1]
        content = file.readline()


    for i in message.keys():
        save.write(message[i]+'\n')
    print(name,"--Sample=",len(message))
    file.close()
    save.close()

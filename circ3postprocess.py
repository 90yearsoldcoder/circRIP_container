import os
import errno
import csv
import sys
import shutil
import argparse

class circ2circRip:
    # copy the result bsj.bed and align files to inputdata folder
    # and modify the bsj file according to the format of circRip
    def __init__(self, sample_name, folder_path):
        #path to circexplore3 result folder
        self.bsj_path = os.path.join(folder_path, "circ/bsj.bed")
        self.align_path = os.path.join(folder_path, "hisat/align.bam")
        self.sample_name = sample_name
        
        #print(self.bsj_path)
        
        if os.path.isfile(self.bsj_path):
            print(self.bsj_path, "is found")
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.bsj_path)
        
        if os.path.isfile(self.align_path):
            print(self.align_path, "is found")
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.align_path)
    
    def writeNewBed(self):
        csv.field_size_limit(sys.maxsize)
        output_file_path = os.path.join(self.inputdata_folder, self.sample_name + ".circ")
        
        
        with open(self.bsj_path, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:

            tsv_reader = csv.reader(infile, delimiter='\t')
            tsv_writer = csv.writer(outfile, delimiter='\t')
            
            tmp_counter = 0
            for row in tsv_reader:
                tmp_counter+=1;
                # Extract the first 4 columns
                first_4_columns = row[:4]

                # Modify the 4th column (index 3) by keeping the number after "/"
                if '/' in first_4_columns[3]:
                    first_4_columns[3] = first_4_columns[3].split('/')[-1]

                # Write the modified row to the output TSV file
                tsv_writer.writerow(first_4_columns)
            
            print("total", tmp_counter, "lines in bsj.bed")
    
    def copyAlign(self):
        dst = os.path.join(self.inputdata_folder, self.sample_name + ".bam")
        print("start copying align file")
        shutil.copyfile(self.align_path, dst)
        print("copy done")
    
    def run(self):
        self.inputdata_folder = os.path.join("./","inputdata")
        os.makedirs(self.inputdata_folder, exist_ok=True)
        self.writeNewBed()
        self.copyAlign()

if __name__ == "__main__":
    
    # a typical command: python circ3postprocess.py -p /restricted/projectnb/ncrna/minty/EP4/input/result -n WB_LJ_PS_EX2_33_S33_L001
    
    # Create the parser
    parser = argparse.ArgumentParser(description="Preprocess the cirexplore3 result into CircRIP input format")
    
    # Add the arguments
    parser.add_argument('-p', metavar='path', type=str, help='the path to result folder')
    parser.add_argument('-n', metavar='name', type=str, help='the name of the sample')
    
    # Execute the parse_args() method
    args = parser.parse_args()
    
    print("The path to result file is: ", args.p)
    print("The name of the file is ", args.n)
    
    #excute process
    
    folder_path = os.path.join(args.p, args.n)
    name = args.n
    Process = circ2circRip(name, folder_path)
    Process.run()
    
    
    
    #test block
    '''
    folder_path_bg  = "/restricted/projectnb/ncrna/minty/EP4/input/result/WB_LJ_PS_EX2_33_S33_L001/"
    name_bg = "WB_LJ_PS_EX2_33_S33_L001"
    bg = circ2circRip(name_bg, folder_path_bg)
    bg.run()
    folder_path_ip = "/restricted/projectnb/ncrna/minty/EP4/elute/result/WB_LJ_PS_EX2_49_S49_L001/"
    name_ip = "WB_LJ_PS_EX2_49_S49_L001"
    ip = circ2circRip(name_ip, folder_path_ip)
    ip.run()
    '''
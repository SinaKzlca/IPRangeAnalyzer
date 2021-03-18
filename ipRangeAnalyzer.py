# Imports
import re
import sys
import argparse
from os import system, name 

# IPv4 Address Pattern
startIPRegex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])"
endIPRegex = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$"

# Other Variables
clear_line = "\033[A                                                     \033[A"
completed_msg = 'completed.'

def writeOutput(ip_list, output_file_path):
    '''
    Writes Extracted IP To Output
    '''
    with open(output_file_path, mode='a+') as f:
        for ip in ip_list:
            f.write(str(ip)+ '\n')
        f.close()

def readInputFile(input_file_path):
    '''
    Reads And Returns IP Ranges In Text File
    '''
    with open (input_file_path, 'r', encoding='utf-8') as f:
        ip_ranges = f.readlines()
    return ip_ranges

def clear():
    '''
    Clear Python Console At The End
    '''
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear') 

def analyzeIPR(ip_ranges):
    '''
    1. Extracts Every Possible Ips Between Start Ip And End Ip Ranges.
    2. Prints Status
    '''
    # Requirements for printing status ---
    total_lines = 0
    complated = 0
    for ip_range in ip_ranges:
        total_lines += 1
    #-------------------------------------

    # Algorithm for analyze ip range --------------------------------------------
    for ip_range in ip_ranges:
        matches = re.finditer(startIPRegex, ip_range, re.MULTILINE)
        for matchNum, matchStart in enumerate(matches, start=1):
            startIP = matchStart.group()
            digit1 = int(matchStart.group(1))
            digit2 = int(matchStart.group(2))
            digit3 = int(matchStart.group(3))
            digit4 = int(matchStart.group(4))
        matches = re.finditer(endIPRegex, ip_range, re.MULTILINE)
        for matchNum, match2 in enumerate(matches, start=1):
            endIP = match2.group()
        IP = (str(digit1)+'.'+str(digit2)+'.'+str(digit3)+'.'+str(digit4))
        if IP == startIP:
            ip_list = []
            while IP != endIP:
                IP = (str(digit1)+'.'+str(digit2)+'.'+str(digit3)+'.'+str(digit4))
                digit4 = digit4 + 1
                ip_list.append(IP)
                if digit4 > 255:
                    digit4 = 0
                    digit3 = digit3 + 1
                    if digit3 > 255:
                        digit4 = 0
                        digit3 = 0
                        digit2 = digit2 + 1
                        if digit2 > 255:
                            digit4 = 0 
                            digit3 = 0
                            digit2 = 0
                            digit1 = digit1 + 1
                            if digit1 > 255:
                                pass
            yield ip_list
    
        #----------------------------------------------------------------------------

        # Prints status -----------------------------------------------------------------------------------------
        complated = complated + 1
        zarib = total_lines/100
        percentage = complated/zarib
        print(clear_line)
        print(str(total_lines)+'/'+str(complated)+' %'+str(round(percentage))+' '+startIP+' >  '+endIP )
        #--------------------------------------------------------------------------------------------------------

def main(output_file_path, input_file_path = None, input_ip_range = None):
    if input_file_path is not None:
        ip_ranges = readInputFile(input_file_path)
        for ip_list in analyzeIPR(ip_ranges):
            writeOutput(ip_list, output_file_path)
        clear()
        print(completed_msg)
    else:
        for ip_list in analyzeIPR(input_ip_range):
            writeOutput(ip_list, output_file_path)
        clear()
        print(completed_msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", help="set output file path.")
    parser.add_argument("--input", "-i", help="set input file path.")
    parser.add_argument("--iprange", "-ipr", nargs='+' , help="import ip range.")
    args = parser.parse_args()
    if not args.output:
        raise IndexError('output path must be supplied on the command line')
    else:
        if (args.input or args.iprange):
            main(output_file_path=args.output, input_file_path= args.input, input_ip_range=args.iprange)
        else:
            raise IndexError('ip range should be supplied via file or command line')
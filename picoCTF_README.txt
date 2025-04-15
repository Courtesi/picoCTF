
[1mWelcome to the picoCTF webshell![0m

[1mUse the arrow keys or spacebar to scroll, or type [1;36mq[1;37m to exit.[0m

This is a browser-accessible Linux shell that can be used for solving
picoCTF challenges.

Note that using the webshell is not necessary for solving challenges.
All files and programs are either available for download or accessible
via remote ports. It is intended primarily for users who do not
have access to their own local shell environment, such as students using
school-provided hardware.

The webshell has many common tools for solving CTF challenges available.
Due to restrictions in the webshell, it is generally not possible to
install additional software. However, if there is a specific tool that
you feel would be helpful to include, send a note on Discord or to
other@picoctf.org and we will consider adding it.

There are various restrictions in place to prevent abuse of the webshell.
Some resource limits can be checked by typing [0;36musage[0m. Note that all
webshell sessions are subject to logging and monitoring, so please do
not enter any sensitive information. Abuse of the webshell infrastructure
is grounds for account termination and disqualification.


[1m# General shell tips for beginners[0m


- Your current directory is displayed in the shell prompt.

- [0;36m~[0m represents your home directory, which is a good place to store
  files you are working on. You can find your way back here at any time by
  typing [0;36mcd ~[0m. Files stored outside of your home directory will not
  persist between webshell sessions.

- Some files are too big to store in your home directory! If you need
  them to work on a challenge, try storing them in [0;36m/tmp[0m, but note that 
  they will not be persisted between webshell sessions.

- Type [0;36mls[0m to list the files in the current directory.

- Type [0;36mcd <path>[0m to change the current directory to that path. Paths are
  relative to the current directory, or absolute if prefixed with [0;36m/[0m.
  Type [0;36mcd ..[0m to go up one level from the current directory.

- Type [0;36mcat <file>[0m to print the contents of a text file.

- Type [0;36m./<file>[0m to run an executable file in the current directory.
  You may first need to grant yourself permission to execute it by
  typing [0;36mchmod +x <file>[0m.

- Type [0;36m<Control-C>[0m to terminate a running process.

- Type [0;36mman <command>[0m to learn more about any command. You can exit
  a manual page by pressing [0;36mq[0m.

- If your terminal prompt starts behaving strangely, type [0;36mreset[0m to
  clear the screen.

- You can end a webshell session by typing [0;36mexit[0m or by closing the tab.


[1m# Tips for solving challenges[0m


- Some challenges require downloading files. Rather than clicking the
  link, you can download the file into the webshell using [0;36mwget[0m, e.g.
  [0;36mwget <file-URL>[0m. Right-click the link to copy the file's URL.

- Some challenges require connecting to a remote port. This is generally
  done using netcat, e.g. [0;36mnc <server-name> <port>[0m. However, certain
  challenges may require the use of programs other than netcat.

- While most challenges are solvable using the webshell, some may be
  difficult or impossible without additional resources. For example,
  some challenges are intended to be solved using GUI programs.

- Exporting files from the webshell to the browser or vice versa
  is possible using [0;36msz <filename>[0m / [0;36mrz[0m.


[1m# Additional notes[0m


- You can connect to the webshell from multiple tabs / devices, and they
  will share the same session. However, note that closing *any one*
  of these tabs will end your webshell session on all of them.

- If you see the message "Killed", a long-running process has been killed
  in order to ensure a fair distribution of resources to all players.
  Extensive brute-forcing is not necessary to solve picoCTF challenges.

- If you see other unexpected errors, you may be running into one of the
  webshell resource limits. Check the [0;36musage[0m command, or, if necessary,
  end your current session using [0;36mexit[0m.

- If you change your username through the picoCTF website, you will
  have a newly created home directory the next time you sign into
  the webshell. However, files from your previous username are still
  accessible under [0;36m/home/<old-username>[0m.


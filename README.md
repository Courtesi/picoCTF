# Courtesi's picoCTF gym

Welcome to the picoCTF webshell!

Use the arrow keys or spacebar to scroll, or type q to exit.

## Usage

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
Some resource limits can be checked by typing usage. Note that all
webshell sessions are subject to logging and monitoring, so please do
not enter any sensitive information. Abuse of the webshell infrastructure
is grounds for account termination and disqualification.

## General shell tips for beginners

- Your current directory is displayed in the shell prompt.

- ~ represents your home directory, which is a good place to store
  files you are working on. You can find your way back here at any time by
  typing cd ~. Files stored outside of your home directory will not
  persist between webshell sessions.

- Some files are too big to store in your home directory! If you need
  them to work on a challenge, try storing them in /tmp, but note that 
  they will not be persisted between webshell sessions.

- Type ls to list the files in the current directory.

- Type cd <path> to change the current directory to that path. Paths are
  relative to the current directory, or absolute if prefixed with /.
  Type cd .. to go up one level from the current directory.

- Type cat <file> to print the contents of a text file.

- Type ./<file> to run an executable file in the current directory.
  You may first need to grant yourself permission to execute it by
  typing chmod +x <file>.

- Type <Control-C> to terminate a running process.

- Type man <command> to learn more about any command. You can exit
  a manual page by pressing q.

- If your terminal prompt starts behaving strangely, type reset to
  clear the screen.

- You can end a webshell session by typing exit or by closing the tab.

## Tips for solving challenges

- Some challenges require downloading files. Rather than clicking the
  link, you can download the file into the webshell using wget, e.g.
  wget <file-URL>. Right-click the link to copy the file's URL.

- Some challenges require connecting to a remote port. This is generally
  done using netcat, e.g. nc <server-name> <port>. However, certain
  challenges may require the use of programs other than netcat.

- While most challenges are solvable using the webshell, some may be
  difficult or impossible without additional resources. For example,
  some challenges are intended to be solved using GUI programs.

- Exporting files from the webshell to the browser or vice versa
  is possible using sz <filename> / rz.

## Additional notes

- You can connect to the webshell from multiple tabs / devices, and they
  will share the same session. However, note that closing *any one*
  of these tabs will end your webshell session on all of them.

- If you see the message "Killed", a long-running process has been killed
  in order to ensure a fair distribution of resources to all players.
  Extensive brute-forcing is not necessary to solve picoCTF challenges.

- If you see other unexpected errors, you may be running into one of the
  webshell resource limits. Check the usage command, or, if necessary,
  end your current session using exit.

- If you change your username through the picoCTF website, you will
  have a newly created home directory the next time you sign into
  the webshell. However, files from your previous username are still
  accessible under /home/<old-username>.

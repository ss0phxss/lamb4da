# lamb4da
A security monitoring wrapper, an addition to the lambda function.

The idea behind the code came from the vulnerabilities found in Lambda environments that can be exploited. The main vulnerability was the unsecure code that allowed RCE exploitations on the containers. Even tho it is impossible to secure every lambda function, it is possible to try and discover suspicious findings in the environment. 

Main abilities of the script are:
1 - Creating a snapshot of the current state of the container's /tmp directory (usualy the only writable directory in those restricted environments). 
2 - Creating a snapshot of the current state of the container's environment variables (usualy fixed by AWS).
(Taking a snapshot will allow us later to compare if any suspicious attributes were added during the execution, due to exploitation of vulnerable code/CVE.)
3 - Seccheck function compares the files after the execution of the main function, if found suspicious findings, it reports.
4 - Safe_lmbd is a decorator, a wrapper. It first runs the secchheck, then the real function, then checks how long it was. If it was longer than (for example) 5 secconds, it prints a warning.
(Measuring the execution time will detect if there are any suspicious processes, that delay the execution of the main function.)
5 - Handler is the real lambda function that we protect.

How to use:
Just add the script to your python lambda function.

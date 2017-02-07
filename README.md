# Internship

## About
Code I used/created for my internship at a security company.

I wrote a script to interact with an exploited host which runs
nginx 1.4.0 for a demonstration environment showing the attack in
[AlienVault](https://www.alienvault.com/).

### What it does
the demo script '''demo.py''' calls the bash scripts to set up the environment for the
exploit, after which it starts a listener '''listen.sh'''. It then goes through the
3 parts of exploitation: Remote code execution, privilege escalation and getting persistent.

## Acknowledgements
* [Robin Verton](https://github.com/rverton) - cowroot (priv-esc tool for CVE-2016-5195).
* [vnsecurity](http://www.vnsecurity.net/) - nginx 1.4.0 x64 exploit.
* [SCS Stanford](http://www.scs.stanford.edu/brop/) - IP fragmentation router.

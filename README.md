<h1>Busybox-telnetd Bruteforcer(BusyBrute)</h1>


<h2> ⚠︎ DISCLAIMER ⚠︎ </h2>

<h3>Legal/ethical use only!</h3>

<p>Use this tool exclusively against systems you own or to systems you have written authorization.
  Unauthorized access to computer systems is illegal in most jurisdictions.
</p>

<h2>what is BusyBrute?</h2>
<p>A multi-threaded credential brute-forcer that targets the <b>"BusyBox Telnetd"</b> service usually on port 23.
BusyBox Telnetd uses a 3 attempt per session system (allows only 3 credentials per session) this script works around
that system and allows the user to automate the task of connecting/disconnecting and trying multiple credentials from
a given wordlist.
  BusyBrute also uses multi-threading to compromise for the slow responses given by the service to verify if the 
credential is correct or not.
</p>

<h2>How does it work?</h2>

<p>
  Busybrute works by:
  
  1. Loading username and password from wordlists given by the user.
  2. Creating telnet connections to the given target.
  3. Attempting authentication using supplied credentials.
  4. Handling the limited number of attempts per session
  5. Using multiple threads to speed up the process.
  6. Reporting when the script gets the credentials or fails. 
</p>

<h2>How to use BusyBrute?</h2>

<p>To use this tool first you need to download the python script on this repo called <b>"BusyBrute.py"</b> <br> or just clone this repo:
  <br>
  <pre><code>git clone https://github.com/J-mikyas/BusyBrute-BusyBox-telnetd-Bruteforce-.git BusyBrute</code></pre>
  <br>
this will clone the repo in your current directory, then navigate to the BusyBrute directory:
  <br>
  <pre><code>cd ./BusyBrute</code></pre>
  <br>

  <p>then excute the script:</p>
  <br>
  <pre><code>python BusyBrute.py [IP] [User Wordlist] [Password Wordlist] [Threads]  </code></pre>
  <br>
  <p>Example:</p>
  <br>

  <pre><code>python BusyBrute.py 192.168.10.1 ./users.txt ./passwords.txt 10</code></pre>

  <p> 
    this example uses the following variables: <br> <br>
      ip - <code>192.168.10.1</code> <br>
      username wordlist - <code>./users.txt</code> <br>
      password wordlist - <code>./passwords.txt</code> <br>
      number of threads - <code>10</code><br>
  </p>

  <p>
    if the script finds the proper credentials it will output the following: <br>
    <pre><code> [+] CREDENTIALS FOUND!: username:password</code></pre><br>
    if the script fails to find the proper credentials it will output the following: <br>
    <pre><code>[!] COULDNT FIND THE CREDENTIALS, TRY A DIFFRENT WORDLIST?</code></pre> <br>
  </p>
</p>



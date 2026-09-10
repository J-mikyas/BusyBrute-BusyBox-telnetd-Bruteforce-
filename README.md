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

<h2>how to use BusyBrute?</h2>

<p>To use this tool firs you need to download the python script on this repo called <b>"BusyBrute.py"</b> <br> or just clone this repo:
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
</p>

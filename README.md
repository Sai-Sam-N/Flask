# Flask Notes

- Flask - Python web framework that can be used for developing web applications. Also for creating web apis, creating ML applications where you're developing a lot of end to end projects
- Developed by Armin Ronacher. Leads a group of International Python enthusiasts / developers named Pocco. 
- Flask is based on WSGI concepts and JINJA2 template engine.
- WSGI : Web Server Gateway Interface. A standard / a protocol. <br>
Explanation: Web applications are hosted in a web server (Apache, IIS). Whenever a request to access the hosted a web application is sent to the web server, a request is sent from the web server to the web application. Now there will be a standard or a protocol by which this request & response communcation happens between the web server and the web application. For this communication, we use something known as WSGI (Web Server Gateway Interface). The web application will contain callable functions, APIs, functionalities which would get called and the response will be received at the web server's end.
![alt text](image.png)
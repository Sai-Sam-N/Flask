# Flask Notes

- Flask - Python web framework that can be used for developing web applications. Also for creating web apis, creating ML applications where you're developing a lot of end to end projects
- Developed by Armin Ronacher. Leads a group of International Python enthusiasts / developers named Pocco. 
- Flask is based on WSGI concepts and JINJA2 template engine.
- WSGI : Web Server Gateway Interface. A standard / a protocol. <br>
<b>Explanation</b>: Web applications are hosted in a web server (Apache, IIS). Whenever a request to access the hosted a web application is sent to the web server, a request is sent from the web server to the web application. Now there will be a standard or a protocol by which this request & response communcation happens between the web server and the web application. For this communication, we use something known as WSGI (Web Server Gateway Interface). The web application will contain callable functions, APIs, functionalities which would get called and the response will be received at the web server's end.
<br>
![](image.png)
<br>
- JINJA2 : a Web templating system. It basically combines a web tempalte along with a certain data source. The data source will dynamically put the data into the template and render the dynamic page. <br>
<b>Example </b>: Suppose we have a ML application, whose aim is to classify whether the given image is a cat or a dog. The image is to be uploaded and submitted via the web page, at the backend level, it is processed by the ML model (either the pickle file or the .h5 file of the ML model) and upon submission, the response (here, the output of the ML model) is to be displayed on the webpage `dynamically` (the web page is dynamically rendered). 
<br>
![https://youtu.be/4L_xAWDRs7w?list=PLZoTAELRMXVPBaLN3e-uoVRR9hlRFRfUc&t=550](image-1.png)
<br>
- Since the `POCCO Group` is heading all of this, the WSGI and JINJA2 are called `POCCO PROJECTS`.

### Creating an environment (for the project)
Overview: If needed, an environment is to be created and you gotta launch vs code in that environment. This guy had done it via anaconda. But Imma do it from my VS Code. For any future probable errors - Jai Maatha Di!
<br>
Apparently whenever this guy lears something, he creates an environment. Not me brother.
<br>
![https://youtu.be/0l9Pu4dk89c?list=PLZoTAELRMXVPBaLN3e-uoVRR9hlRFRfUc&t=155](image-2.png)
<br>
`activate myenv` : activates an environment called 'myenv' at the current path
`code .` : opens and launches VSCode at the current folder
<br>
- [Read more](https://dev.to/mursalfk/setup-flask-on-windows-system-using-vs-code-4p9j)

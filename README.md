# Instagram---Python

# Instalación 
pip install python-instagram

# Obtener client ID
Dirigirse https://www.instagram.com/developer/ y dar click en el botón "Manage Clients", luego de esto ingresar los datos que se le piden.
En la casilla de website URL usted puede poner cualquier url, pero en "Valid redirect URIs" que especifica a dónde redirigimos a los usuarios después de que hayan elegido si autenticar o no su aplicación, en nuesto caso "localhost:3000/.

# Obtener access token
para obtener el access token debemos dirigirnos a la url https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token, en CLIENT_ID colocamos el client id que nos aroja cuando creamos un clien y en REDIRECT-URI colocamos http://localhost:3000/ y damos enter, a continuación pedirá una autorización, luego de autizar obtendremos nuestro access token de esta manera http://localhost:3000/#access_token=138046...

# Importar API en Python
para usar la api solo debemos de poner from instagram.client import InstagramAPI

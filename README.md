# SPRINT 7

## PRUEBAS AUTOMATIZADAS 

## URBAN ROUTES

Es una plataforma donde puedes rentar un servicio pro de trasporte comuni llamado taxi, el cual podras tener servicio de
calidad, seleccionando el origen y el destino tendras de inmediato una tarifa del servicio, al memoento podras seleccionar
tu necesidad y comididad del viaje, en este caso ocuparemos comfort para esta prueba, segun nuestros requisitos y con los
datos que nos hicieron llegar en data.py donde se muetra las direcciones, el numero de telefono, forma de pago, y pedir 
el taxi.

Al final de la prueba se muetra los detalles del servicio obtenido de la informacion determinada, como la foto del conductor,
las placas del veiculo, el precio, el destino y el origen, y en canto tiempo llegara por ti.



## DESARROLLO TECNOLOGICO

En estas pruebas automatizadas ocupamos el lenguaje Python con herramienta Pycharm, dentro de la herramienta pycharm ocupamos
del su paquete selenium web driver y para revisar las pruebas ocupamos chrome con Versión 121.0.6167.184 (Build oficial) (64 bits).


## TECNICAS OCUPADAS PARA ESTA AUTOMATIZACION 

Ocupamos busquedas necesarias de elementos por ejemplo por ID, CSS_SELECTOR, Xpath,entre otros.
 Tambien usamos el metodo POM (Page Object Model)

## EJECUCION DE LAS PRUEBAS

Para poder hacer las pruebas necesites tener en pycharm instalado selenium, pytest ña cual las puedes instalar con 
python packages, o con la consola escribiendo: pip install selenium.

para la automatizacion tendras los archivos retrieve_phone_code.py el cual te dara el codigo de acceso del telefono o el SMS-code,
tambien tendras otro archivo llamado UrbanRoutesPage.py el cual te dara la accion de la pagina, siguiendo los archivos tendras 
otro llamado data.py el cual trae los datos que debemos ocupar para hacer funcionar la pagina, y final el main.py este contiene 
la comprobacion de cada paso para la ejecucion de la pagina; en este solo podras correr la prueba, con la URL proporcionada por 
TripleTen. 

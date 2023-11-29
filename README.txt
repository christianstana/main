Ejecución de Pruebas
El proyecto utiliza Pytest para realizar pruebas. Ejecuta las pruebas con el siguiente comando:

bash
Copy code
pytest main.py -vv
Linting con Flake8
Flake8 se utiliza para el linting del código. Ejecuta el linting con:

bash
Copy code
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
Resultados de las Pruebas
Después de ejecutar las pruebas, los resultados se almacenan en el archivo test_results.txt. Este archivo se utiliza para determinar si las pruebas fueron exitosas o si hubo algún fallo.

Publicación en README.txt
En caso de que las pruebas fallen, se generará un informe en el archivo README.txt indicando que las pruebas han fallado y proporcionando detalles sobre el commit en el que ocurrió el fallo. En caso de éxito, se indicará que las pruebas han pasado con la versión v1.0.1.

Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras errores o mejoras potenciales, no dudes en abrir un problema o enviar una solicitud de extracción.

Licencia
Este proyecto está bajo la Licencia [Nombre de la Licencia] - consulta el archivo LICENSE.md para obtener más detalles.

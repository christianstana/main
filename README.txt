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

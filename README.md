# Campus-Validador-Correo-Simple
Estás trabajando en un formulario de registro de nuevos usuarios y necesitas una primera capa de validación para los correos electrónicos. Tu tarea es crear una función que realice una revisión básica del formato de un correo electrónico para descartar las entradas obviamente incorrectas.



Debes crear una única función llamada es_correo_valido que acepte un string (el correo) como parámetro y retorne True si cumple con todas las siguientes reglas, o False si falla al menos una.



Reglas de Validación:

Debe contener un único símbolo de arroba ("@").
El símbolo de arroba no puede ser el primer ni el último carácter.
Debe haber al menos un punto (".") después del símbolo de arroba.
El punto no puede estar inmediatamente después del símbolo de arroba.
El punto no puede ser el último carácter del correo.


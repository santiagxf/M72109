===========
Anotaciones
===========

Uno de los atribútos más importante en aquellos modelos de aprendizaje automático supervisados es la variable a predecir o target. Esto en general lo llamamos "anotaciones". Dependiendo del problema que estamos tratando de resolver será el típo de anotaciones que deberemos suministrar. Notará que en algunos casos suministrar una anotación puede ser una tarea sencilla, pero en otros casos podría suponer una cantidad sustancial de tiempo e incluso y elemento de diseño de modelo de aprendizaje automático.


Problemas de detección de objetos
---------------------------------

En los problemas de detección de objetos estamos interesados en obtener la ubicación específica de cada uno de los objetos dentro de una imágen. En estos problemas, las anotaciones se indican como "cajas" que continen el objeto en cuestión. Estas cajas se las suele llamar **bouding-boxes** o **ROI - Region of interest**.

Existen muchas herramientas para generar estas anotaciones, aunque una de las más simples es `labelImg`.
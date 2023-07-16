Grandes Modelos de Lenguaje (LLM)
=================================

Los grandes modelos de lenguaje o LLM (por las siglas en ingles de Large Language Models) han revolucionado recientemente la industria y en general la forma en que se resuelven, no solo los problemas de procesamiento de texto, sino que cualquier tipo de problemática que pueda ser descripta por medio de la utilización del lenguaje.

.. note::
   Si le interesa una revisión de los diferentes avances que se mencion en este curso y como los mismos contribuyeron al estado del arte en NLP hasta los grandes modelos de lenguaje, recomendamos la lectura del blog (en inglés) `It wasn’t Magic. How NLP went from Text Mining to the Era of Large Language Models <https://santiagof.medium.com/it-wasnt-magic-how-nlp-went-from-text-mining-to-the-era-of-large-language-models-6e962af26719>`_.

Introducción
------------

Conceptualmente, los grandes modelos de lenguaje no se desprenden de la idea de :doc:`language-models` que vimos hasta el momento. Los mismos modelan la ditribución probabilística de una secuencia de palabras o tokens. Sin embargo, la diferencia en su eficacia radica en la palabra **grandes**. Las arquitecturas basadas en :doc:`transformers` han demostrado disponer de una amplia capacidad para modelar complejas distribuciones de datos. Esta capacidad hizo que, disponiendo de suficiente capacidad de procesamiento y de suficiente cantidad de datos, los modelos puedan escalar en terminos de la cantidad de parámetros que utilizan. Más aún, se demostró empiricamente que dada una misma arquitectura de modelo, la cantidad de parámetros es proporcional a las habilidades que podemos ver que el modelo exhibe.

Características
~~~~~~~~~~~~~~~
Los grandes modelos de lenguaje se diferencian de los modelos de lenguaje tradicionales en una característica que los hace muy distintos al utilizar en la práctica. Estos modelos (en general) no requieren un proceso de fine-tuning para adaptor a otro domonio. Los mismos pueden generalizar facilmente para resolver otro tipo de problemas distintos a los que fueron originalmente entrenados.

Conjunto de datos
-----------------
Como mencionamos, los grandes modelos de lenguaje disponen de una cantidad elvada de parámetros. Poder estimar estos parámetros eficientemente require de un conjunto de datos acorde. Por ejemplo, el modelo LLaMA (entrenado por Meta en Febrero 2023), es un modelo con variantes que van desde los 7 mil millones (billones en inglés) a los 65 mil millones de parámeteros. Este modelo fué entrenado con un conjunto de datos de 1.2 billon (trillon en inglés) de tokens.

Claramente collectar, curar, y disponibilizar conjuntos de datos de estas características es complejo. Incluso, las organizaciones que entrenan estos modelos no siempre proporcionan información sobre las carácteristicas de los conjuntos de datos ya que representan una ventaja competitiva. Sin embargo, si sabemos que la calidad de los modelos está relacionada con la cantidad y calidad de los datos. Afortunadamente, internet es una fuente de una amplia cantidad de información en formato texto lo cual permite el entrenamiento de estos grandes modelos de aprendizaje y virtualmente todos los grandes modelos de lenguaje utilizan conjuntos de datos públicos en una forma más que significativa. No pierda de vista, de todos modos, que muchos modelos disponen de conjuntos de datos especificos y más puntuales que le otorgan determinadas capacidades que quizas otros no disponen.

Prompt engineering
------------------
Los grandes modelos de lenguaje son extremadamente buenos en modelas una secuencia de texto y, por lo tanto, predecir (o generar) una secuencia de texto coherente que podría continuar el texto provisto. Este modo de utilización de un modelo de aprendizaje automático de texto se conoce como **completions**. Lo interesentante de esta modalidad es que, al ser la entrada una cadena de texto en lenguaje natural, uno podría en teoría estructurar una secuencia de texto que, cuando el modelo la complete, resuelva el problema en cuestión. Por ejemplo, en los ejemplos de clasificación de tweets que hemos visto, uno podría generar un texto comoÑ

   "El usuaio <usuario> publico en su feed: <tweet original>. Este tweet hace referencia a ..."

La siguiente palabra que el modelo predice probablemente sea una descripción de a que hace referencia este tweet. Claro esta, que esta frase puede ser completada de muchas maneras (tantas como palabras existen en el vocabulario). Podríamos reducir la probabilidad de que el modelo prediga algo que no queremos modificando la estructura del texto:

   "El usuaio <usuario> publico en su feed: <tweet original>. Considerando las cátegorias ALIMENTACIÓN, DEPORTES, y RETAIL, este tweet hace referencia claramente a ...".

Recuerde que los modelos de lenguaje modelan la distribución probabilistica de una determinada cadena de texto. Si las categorías que queremos que mencione estan dentro del texto, entonces existe una mayor probabilidad de que el texto haga referencia a alguna de las categorías mencionadas. Si quiere ver una ejemplo más extremo pero más fácil de visualizar, en el texto "del 1 al 10, este restorante es un 17", la palabra "17" debería tener una probabilidad mucho mas baja que cualquier numero entre 1 y 10. 

Esta realidad de los modelos de lenguaje hace que los desarroladores pasen una buena cantidad de tiempo en diseñar el texto o plantilla correcta con el cual proveer un modelo de lenguaje para resolver el cometido. Esta práctica de buscar la mejor estructura de texto, o **prompt**, con la cual pedirle al modelo que genere un **completion** se conoce como **Prompt Engineering**.


Aliniamiento (alignment)
------------------------
Aliniamiento o **alignment** hace referencia al problema de alinear la intención u objetivo que una persona tiene al utilizar un modelo de aprendizaje automático con las heurística y reglas con las que efectivamente el modelo opera en realidad. El problema de alignment es complejo dado que no es tan sencillo de identificar, incluso cuando el usuario obtiene lo que espera (a priori) como resultado. Alignment es un problema que se encuentra en activa investigación actualmente y que, claramente, no está resuelto.

Una de las técnicas que han contribuido a mejorar la capacidad de aliniamiento es la técnica Reinforcement Leanring with Human Feedback (RLHF). En términos simples, RLHF entrena modelos vía fine-tuning aprendiendo de las preferencias de las personas al calificar sus respuestas. Si un modelo hace una predicción o realiza una acción incorrecta o subóptima, se puede usar la retroalimentación para corregir el error o sugerir una mejor respuesta. Con el tiempo, esto ayuda al modelo a aprender y mejorar sus respuestas. RLHF se usa en tareas en las que es difícil definir una solución algorítmica clara, pero en las que las personas pueden juzgar fácilmente la calidad de la salida (por ejemplo, si la tarea es generar una historia convincente, una persona pueden calificar diferentes historias generadas según su calidad).

Más precisamente, RLHF es una técnica que entrena un "modelo de recompensa" directamente a partir del feedback de personas y utiliza el modelo como una función de recompensa para optimizar una política mediante aprendizaje reforzado. Este feedback se recopila comúnmente pidiéndole directamente a personas que clasifiquen instancias de differentes **completions**.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos
   :hidden:

   Few-shot learning <few_shot_classification.ipynb>

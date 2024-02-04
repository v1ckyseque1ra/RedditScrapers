<h1 class="code-line" data-line-start=4 data-line-end=5 ><a id="Reddit_Scrapers_4"></a>Reddit Scrapers</h1>
<p class="has-line-data" data-line-start="6" data-line-end="7">Este repositorio contiene dos scrapers de Reddit escritos en Python para obtener información de subreddits específicos. Los scrapers son herramientas simples pero efectivas para extraer datos de hilos y comentarios en Reddit.</p>
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Scraper_1_8"></a>Scraper 1:</h2>
<p class="has-line-data" data-line-start="10" data-line-end="11">El primer scraper (<code>reddit.py</code>) está diseñado para recuperar los títulos, autoress, URLs, puntajes y numero de comentarios de los 10 últimos posteos del subreddit que ingrese el usuario.</p>
<h3 class="code-line" data-line-start=12 data-line-end=13 ><a id="Instrucciones_12"></a>Instrucciones</h3>
<ol>
<li class="has-line-data" data-line-start="14" data-line-end="15">Abre el archivo <code>reddit.py</code> en tu editor de código preferido.</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Ejecuta el script en tu terminal o entorno de ejecución Python y responde con tu reddit preferido.</li>
<li class="has-line-data" data-line-start="16" data-line-end="18">Observa cómo el programa imprime los títulos de los hilos más recientes en el subreddit.</li>
</ol>
<h2 class="code-line" data-line-start=18 data-line-end=19 ><a id="Scraper_2_Obtener_Comentarios_de_un_Hilo_18"></a>Scraper 2: </h2>
<p class="has-line-data" data-line-start="20" data-line-end="21">El segundo scraper (<code>reddit2.py</code>) se centra en recuperar los comentarios más votados de un hilo específico de Reddit.</p>
<h3 class="code-line" data-line-start=22 data-line-end=23 ><a id="Instrucciones_22"></a>Instrucciones</h3>
<ol>
<li class="has-line-data" data-line-start="24" data-line-end="25">Abre el archivo <code>reddit2.py</code> en tu editor de código preferido.</li>
<li class="has-line-data" data-line-start="25" data-line-end="26">Modifica la variable <code>url</code> con la URL del hilo que deseas analizar.</li>
<li class="has-line-data" data-line-start="26" data-line-end="27">Ejecuta el script en tu terminal o entorno de ejecución Python.</li>
<li class="has-line-data" data-line-start="27" data-line-end="29">Observa cómo el programa imprime los comentarios del hilo seleccionado.</li>
</ol>
<h2 class="code-line" data-line-start=29 data-line-end=30 ><a id="Requisitos_29"></a>Requisitos</h2>
<p class="has-line-data" data-line-start="31" data-line-end="32">Ambos scrapers utilizan la biblioteca <code>praw</code> para interactuar con la API de Reddit. Asegúrate de tener esta biblioteca instalada antes de ejecutar los scripts. Puedes instalarla utilizando:</p>
<pre><code class="has-line-data" data-line-start="34" data-line-end="36" class="language-bash">pip install praw
</code></pre>

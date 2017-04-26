��    6      �  I   |      �     �  )   �     �  d  �  �  Z  .  

  D  9  �   ~  �  J  �   �  N  y      �     �  f     X   h     �     �     �     �     �                       t   %  �   �  
   l     w     �     �     �     �     �     �     �  	   �     �     �       <   '  b   d     �     �     �  =        @  '   Q     y  %   �  /   �     �       	     �         7   0     h    �     �  �  �"     &  e  1*  �  �+    7.  �  :/  &   1  &   A1  �   h1  �   '2     �2     �2     �2     �2     3     3  
   ,3     73     F3    U3  n  c4     �5  "   �5     6  *   +6     V6     g6     �6     �6  !   �6     �6     �6     7  0   7  \   I7  �   �7     g8  I   ~8     �8  ~   �8  1   ^9  1   �9     �9  J   �9  O   -:  *   }:  %   �:  #   �:     !          0              )      (            .          1             $   &      2         '          "                 +   5              #         	                      3              %   ,       
   4      -          *                       /   6          14:30:59 or 14:30 2006-10-25 14:30:59 (YYYY-MM-DD HH:MM:SS) 2017-03-19 (YYYY-MM-DD) <h4><em>Boolean and Choice fields.</em></h4><p>These Django fields let you make a choice. If you want to include a boolean in your form that can be either <strong>True</strong> or <strong>False</strong> (e.g. a checked or unchecked checkbox), you must remember to pass in <strong>required=False</strong> when creating the <strong>BooleanField</strong>.</p> <h4><em>HTML5 input types.</em></h4><p>&quot;If your form includes an URLField, an EmailField or any integer field type, Django will use the url, email and number HTML5 input types. By default, browsers may apply their own validation on these fields, which may be stricter than Django’s validation. If you would like to disable this behavior, set the <strong>novalidate</strong> attribute on the form tag, or specify a different widget on the field, like TextInput&quot; (<a href='https://docs.djangoproject.com/en/1.10/topics/forms/#working-with-forms' target='_blank'>Django Documentation <span class='glyphicon glyphicon-new-window' aria-hidden='true'></span></a>)</p><p>Browsers apply their own validation on these fields. For any integer field <strong>Field.localize</strong> must be <strong>False</strong>. Try to input the wrong value and submit the form - browser validation will warn you about an error in the first wrong field.</p> <h4><em>TextInput based fields.</em></h4><p>These Django fields use <strong>TextInput</strong> as a default widget, so only <em>required</em>, <em>max_length</em> and <em>min_length</em> properties are validated by browsers. Try to input the wrong value and submit the form - browser validation will not warn you  about an error and you will get a Django validation error.</p><div class='panel panel-info'><div class='panel-body'>All <a href='{% url 'portfolio:django_forms' 'date-time-fields' %}'>time and date</a> Django fields use text inputs.</div></div> <h4><em>Time and Date Django fields.</em></h4><p>Django uses <strong>TextInput</strong> as a default widget for date and time fields, so only <em>required</em>, <em>max_length</em> and <em>min_length</em> properties are validated by browsers. Try to input the wrong value and submit the form&nbsp;-&nbsp;browser validation will not warn you  about an error and you will get a Django validation error.</p><p>Each field accepts <strong>format</strong> optional argument. If no format argument is provided the first format found in DATE(TIME)_INPUT_FORMATS settings will be used.</p> <h4>CKEditor.</h4><p>CKEditor is a browser-based WYSIWYG content editor. It brings to the web common word processor features found in desktop editing applications like Microsoft Word and OpenOffice. </p> <h4>Django-tinymce.</h4><p>&quot;Django-tinymce&quot; is a Django application that contains a widget to render a form field as a TinyMCE editor. It uses TinyMCE editor 3.5.11. Current version of TinyMCE editor is TinyMCE&nbsp;4.5.x. and you need only two scripts in HEAD section of HTML document <a href="{% url 'portfolio:tinymce' 'tinymce4' %}">to convert</a> any your field in rich text editor.</p> <h4>NicEdit.</h4><p>NicEdit is a Lightweight, Cross Platform, Inline Content Editor to allow easy editing of web site content on the fly in the browser.</p> <h4>TinyMCE 4.</h4><p>Tiny MCE 4 is a platform independent web-based JavaScript HTML WYSIWYG editor. TinyMCE enables you to convert HTML textarea fields or other HTML elements to editor instances. Current version of TinyMCE editor is TinyMCE&nbsp;4.5.x. and you need only two scripts in HEAD section of HTML document to enable it.</p> A full set of Django form fields All Django form fields. Browser-based WYSIWYG content editors bring to the web features found in desktop editing applications. CSS describes the style, layout of an HTML document and transformation of it's elements. CSS effects Choice fields Contact DateTime fields Django form fields Email.. Forms HTML5 input Home I disabled animation for devices with screen less than 768 pixels. Sorry. Try to view this page with larger monitor. I'm a web developer. I&nbsp;have more or less skills in Python, Django, HTML, CSS, JavaScript, Bootstrap and other web technologies. I worked for a small team and participated in the creation of several sites. Message... My portfolio site Oleg Soloviov Page not found Reset Rich text editors Send Send me your letter. Server Error (500) Subject.. Submit TextInput fields Thank you for your email. Thank you for your email. I will answer as soon as possible. The Django forms library comes with a set of Field classes that represent common validation needs. Time and Date To send a letter fill the form. View details a string which can be converted into a timedelta: DD HH:MM:SS any char or sign digits: 6, decimal places: 2 == 1234.56 float between 1.44 and 3.14 integer between 10 and 100 - required only letters, numbers, underscores, and hyphens string with "foo" substring valid Email valid URL Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2017-04-26 09:35+0000
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language-Team: LANGUAGE <LL@li.org>
Language: russian
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=4; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<12 || n%100>14) ? 1 : n%10==0 || (n%10>=5 && n%10<=9) || (n%100>=11 && n%100<=14)? 2 : 3);
 14:30:59 или 14:30 2006-10-25 14:30:59 (ГГГГ-ММ-ДД ЧЧ:ММ:СС) 2017-03-19 (ГГГГ-ММ-ДД) <h4><em>Поля выбора.</em></h4><p>Эти поля Django позволяют вам сделать выбор. Если вы намерены включить в cвою форму поле <strong>checkbox</strong>, которое может быть либо <strong>True</strong>, либо <strong>False</strong> (т.е. флажок отмечен или нет), то необходимо, определяя поле <strong>BooleanField</strong> установить <strong>required=False</strong>.</p> <h4><em>HTML5 поля.</em></h4><p>&quot;Если в вашей форме есть поля URLField, EmailField, либо одно из цифровых полей, то Django будет использовать HTML5 поля: url, email и number соответственно. По умолчанию, браузеры могут осуществлять свою проверку этих полей, которая может быть даже строже, чем проверка (валидация) Django. Если вы хотите отключить эту проверку, то установите атрибут <strong>novalidate</strong> самой формы, или используйте другой виджет для этого поля, например TextInput&quot; (<a href='https://docs.djangoproject.com/en/1.10/topics/forms/#working-with-forms' target='_blank'>Django Documentation <span class='glyphicon glyphicon-new-window' aria-hidden='true'></span></a>)</p><p>Браузеры осуществляют свою проверку этих полей. Для любого числового поля <strong>Field.localize</strong> должно быть установлено в значение <strong>False</strong>. Попробуйте ввести неправильное значение и отправить форму&nbsp;-&nbsp;браузер предупредит вас об ошибке в первом по счету поле с неправильным значением.</p> <h4><em>Поля на основе TextInput.</em></h4><p>Для этих полей Django использует <strong>TextInput</strong> в качестве виджета по умолчанию, поэтому браузеры проверяют поля только на соответствие свойствам <em>required</em>, <em>max_length</em> и <em>min_length</em>. Попробуйте ввести неверное значение и отправить форму&nbsp;-&nbsp;браузер не предупредит вас об ошибке и вы  получите ошибку валидации Django.</p><div class='panel panel-info'><div class='panel-body'>Все поля Django для <a href='{% url 'portfolio:django_forms' 'date-time-fields' %}'>времени и даты</a> используют <strong>TextInput</strong> виджет по умолчанию.</div></div> <h4><em>Django поля для даты и времени.</em></h4><p>Django использует <strong>TextInput</strong> как виджет по умолчанию для полей даты и времени, поэтому только свойства <em>required</em>, <em>max_length</em> и <em>min_length</em> проверяются браузерами. Попробуйте ввести неверное значение в поле и отправить форму&nbsp;-&nbsp;браузер не предупредит вас о неверном значении и вы увидите только сообшение Django об ошибке.</p><p>В каждом таком поле устанавливается необязательное свойство <strong>format</strong>. Если оно не установлено, то будет использовано первое значение, найденное в переменной DATE(TIME)_INPUT_FORMATS модуля <strong>settings</strong> Django.</p> <h4>CKEditor.</h4><p>CKEditor это браузерный WYSIWYG редактор контента. Он предоставляет для интернета основные черты &quot;больших&quot; десктопных приложений для редактирования текста, таких как Microsoft Word и OpenOffice.</p> <h4>Django-tinymce.</h4><p>&quot;Django-tinymce&quot; это приложение Django, которое содержит виджет, чтобы превратить поле формы в редактор TinyMCE. Используется версия 3.5.11 редактора TinyMCE. Текущая версия TinyMCE редактора&nbsp;-&nbsp;4.5.x. Для его установки нужно только два скрипта в разделе HEAD  HTML документа и ваше поле формы <a href="{% url 'portfolio:tinymce' 'tinymce4' %}">превратится</a> в редактор форматированного текста.</p> <h4>NicEdit.</h4><p>NicEdit это легкий, межплатформенный онлайн редактор, который позволяет легко редактировать содержимое вебсайта прямо в браузере.</p> <h4>TinyMCE 4.</h4><p>Tiny MCE 4 это платформо независимый JavaScript HTML WYSIWYG редактор для интернета. TinyMCE дает возможность превратить поле textarea в полноценный редактор. Текущая версия редактора TinyMCE&nbsp;4.5.x. Чтобы использовать его нужно только два тега scripts разделе HEAD HTML документа.</p> Все поля Django для форм Все поля Django для форм Браузерные WYSIWYG редакторы контента воплощают черты десктопных приложений для редактирования текста.</p> CSS описывает стиль, взаимное расположение и трансформацию элементов документа HTML. CSS эффекты Поля выбора Контакты Время и Дата Поля Django Ваш Email Формы HTML5 поля Главная Извините, но я отключил анимацию для устройств с экраном меньше чем 768 пикселей. Попробуйте открыть эту страницу на устройстве с большим монитором. Я веб разработчик. Обладаю в большей или меньшей степени   навыками в Python, Django, HTML, CSS, JavaScript, Bootstrap и в других веб технологиях. Я работал на маленький коллектив и участвовал  в создании нескольких сайтов.  Ваше сообщение Мой портфолио сайт Соловьев Олег Страница не найдена (404) Очистить Редакторы текста Отправить Отправить письмо Ошибка сервера (500) Тема письма Отправить Поля TextInput Спасибо за Ваше сообщение. Спасибо за Ваше письмо. Я отвечу как можно быстрее. Django фреймворк содержит библиотеку полей HTML форм, реализующих основные случаи проверки (валидации) полей. Время и Дата Чтобы отправить письмо заполните форму. Подробности строка, которая может быть преобразована в <strong>timedelta</strong>: ДД ЧЧ:ММ:СС любой знак, буква или цифра целых: 6, десятичных: 2 == 1234.56 число от 1.44 до 3.14  целое число от 10 до 100 (обязательное поле) только буквы, цифры, подчеркивание или тире строка с подстрокой "foo" правильный Email адрес правильный URL адрес 